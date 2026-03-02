# Instalar dependências no terminal:
# pip install streamlit pandas pyarrow plotly

import os
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Amazon Catalog Intelligence", layout="wide")

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_parquet(path)
    # segurança de tipos
    for c in ["price", "rating", "units_sold_last_month"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

st.title("Amazon Catalog Intelligence & Strategic Analytics")
st.caption("Data App (Streamlit) — camada interativa sobre Silver + Enriched (LLM)")

current_dir = os.path.dirname(__file__)
default_path = os.path.join(current_dir, "amazon_catalog_app.parquet")

DATA_PATH = st.sidebar.text_input(
    "Path do dataset (parquet)",
    value=default_path
)

try:
    df = load_data(DATA_PATH)
except Exception as e:
    st.error(f"Não consegui ler o arquivo: {e}")
    st.stop()

# Filtros
st.sidebar.header("Filtros")

cat = st.sidebar.multiselect(
    "Category",
    options=sorted(df["category_name"].dropna().unique()),
    default=[]
)

seg = st.sidebar.multiselect(
    "Price Segment",
    options=sorted(df["price_segment"].dropna().unique()),
    default=[]
)

tier = st.sidebar.multiselect(
    "Popularity Tier",
    options=sorted(df["popularity_tier"].dropna().unique()),
    default=[]
)

df_f = df.copy()
if cat:
    df_f = df_f[df_f["category_name"].isin(cat)]
if seg:
    df_f = df_f[df_f["price_segment"].isin(seg)]
if tier:
    df_f = df_f[df_f["popularity_tier"].isin(tier)]

# Páginas
tab1, tab2, tab3 = st.tabs(["Executive", "Segmentation", "AI Insights"])

# Página 1: Visão Executiva
with tab1:
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Products", f"{len(df_f):,}")
    col2.metric("Best Sellers", f"{int(df_f['is_best_seller'].sum()):,}" if "is_best_seller" in df_f.columns else "—")
    col3.metric("Avg Price (USD)", f"${df_f['price'].mean():.2f}" if df_f["price"].notna().any() else "—")
    col4.metric("Avg Rating (★)", f"{df_f['rating'].mean():.2f}" if df_f["rating"].notna().any() else "—")

    # Units Sold Last Month (tabela)
    st.subheader("Top Products (by Units Sold Last Month)")

    top = df_f.sort_values("units_sold_last_month", ascending=False).head(25)

    try:
        df = load_data(DATA_PATH)
        
        if "llm_title_clean" in df.columns:
            df = df.rename(columns={"llm_title_clean": "product_title_short"})

    except Exception as e:
        st.error(f"Não consegui ler o arquivo: {e}")
        st.stop()

    show_cols = [
        "product_title_short", "category_name", "price_segment", "popularity_tier",
        "price", "rating", "units_sold_last_month", "is_best_seller",
        "llm_brand_guess", "llm_product_type", "product_url"
    ]

    show_cols = [c for c in show_cols if c in top.columns]

    st.dataframe(top[show_cols], use_container_width=True, height=420)

    # Price vs Rating (scatter)
    st.subheader("Performance Map: Price vs Rating")

    if df_f["price"].notna().any() and df_f["rating"].notna().any():
        df_scatter = df_f.dropna(subset=["price", "rating"]).copy()

        if len(df_scatter) > 20000:
            df_scatter = df_scatter.sample(20000, random_state=42)
        
        color_map = {
            "budget": "#00C853",
            "mid": "#00B0FF",
            "premium": "#AA00FF",
            "luxury": "#FFD600"
        }

        fig = px.scatter(
            df_scatter,
            x="price",
            y="rating",
            color="price_segment" if "price_segment" in df_scatter.columns else None,
            color_discrete_map=color_map,
            category_orders={"price_segment": ["budget", "mid", "premium", "luxury"]},size="units_sold_last_month" if "units_sold_last_month" in df_scatter.columns else None,
            hover_data=[c for c in ["product_title", "category_name"] if c in df_scatter.columns],
            render_mode="webgl",
            title=None
        )

        # Definir limites razoáveis
        max_price_view = df_scatter["price"].quantile(0.92)

        fig.update_xaxes(range=[0, max_price_view])
        fig.update_yaxes(range=[3.4, 5.1])
        fig.update_traces(
            opacity=0.4,
            marker=dict(sizemin=3, sizemode='area', sizeref=2.*max(df_scatter["units_sold_last_month"] if "units_sold_last_month" in df_scatter.columns else [10])/(30.**2))
        )
        fig.update_layout(
            height=520, margin=dict(l=10, r=10, t=10, b=10),
            legend_title_text=None,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Insufficient price/rating data for the current selection.")

# Página 2: Segmentação e Análise de Mix
with tab2:
    col1, spacer, col2 = st.columns([1.35, 0.1, 1])

    # Price Segment (tabela)
    with col1:
        st.subheader("Product Mix: Category × Price Segment")

        if {"category_name", "price_segment"}.issubset(df_f.columns):
            pivot = pd.pivot_table(
                df_f,
                index="category_name",
                columns="price_segment",
                values="product_id" if "product_id" in df_f.columns else "category_name",
                aggfunc="count",
                fill_value=0,
                margins=True,
                margins_name="Total"
            )

            if "Total" in pivot.columns:
                pivot = pivot.sort_values("Total", ascending=False)

            st.dataframe(pivot, use_container_width=True, height=500)
        else:
            st.info("Missing columns for pivot (category_name, price_segment).")

    # Revenue Proxy (barras)
    with col2:
        st.subheader("Revenue Proxy (directional)")

        if {"price", "units_sold_last_month", "category_name"}.issubset(df_f.columns):
            df_tmp = df_f.copy()
            df_tmp["revenue_proxy"] = (
                df_tmp["price"].fillna(0) * df_tmp["units_sold_last_month"].fillna(0)
            )

            rev = (
                df_tmp
                .groupby("category_name", as_index=False)
                .agg({"revenue_proxy": "sum"})
                .sort_values(by="revenue_proxy", ascending=True)
                .tail(15)
            )

            # barra horizontal (mais legível)
            fig_rev = px.bar(
                rev.sort_values("revenue_proxy"),  # crescente para ficar “top” em cima quando horizontal
                x="revenue_proxy",
                y="category_name",
                orientation="h"
            )
            fig_rev.update_layout(height=520, margin=dict(l=10, r=10, t=10, b=10))

            st.plotly_chart(fig_rev, use_container_width=True, height=465)
            st.caption("Proxy = price × units_sold_last_month (não representa receita contábil).")
        else:
            st.info("Missing columns for revenue proxy (price, units_sold_last_month, category_name).")

# Página 3: Insights Enriquecidos por IA
with tab3:
    st.subheader("AI-Enriched Catalog Intelligence")
    st.caption("Baseado em extração via LLM (product_title → brand_guess, product_type, keywords).")

    # ===== Preparação / limpeza =====
    df_ai = df_f.copy()

    # Normaliza strings (evita duplicidade por maiúscula/espaco)
    if "llm_product_type" in df_ai.columns:
        df_ai["llm_product_type"] = (
            df_ai["llm_product_type"]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    if "llm_brand_guess" in df_ai.columns:
        df_ai["llm_brand_guess"] = (
            df_ai["llm_brand_guess"]
            .astype("string")
            .str.strip()
            .str.upper()
        )

    # Calcula revenue_proxy se necessário (e se a métrica escolhida for revenue)
    if {"price", "units_sold_last_month"}.issubset(df_ai.columns):
        df_ai["revenue_proxy"] = (
            pd.to_numeric(df_ai["price"], errors="coerce").fillna(0)
            * pd.to_numeric(df_ai["units_sold_last_month"], errors="coerce").fillna(0)
        )
    else:
        df_ai["revenue_proxy"] = 0.0

    # Helper: remove Unknown/None/NaN
    def _valid_series(s):
        return s.notna() & (~s.isin(["UNKNOWN", "Unknown", "none", "None", "nan", "NaN", ""]))

    # Helper: agrega top N por métrica
    def top_n(df, group_col, n=15):
        if group_col not in df.columns:
            return None

        d = df[_valid_series(df[group_col])].copy()
        if len(d) == 0:
            return None

        # métrica base
        out = (
            d.groupby(group_col, dropna=True)
            .agg(Value=("revenue_proxy", "sum"))
            .reset_index()
            .sort_values("Value", ascending=False)
            .head(n)
        )

        value_label = "Revenue Proxy ($)"

        return out, value_label

    c1, c2 = st.columns(2)

    # Tipos de Produtos (colunas)
    with c1:
        st.markdown("**Top AI-Inferred Product Types**")

        res = top_n(df_ai, "llm_product_type", n=15)

        if res is None:
            st.info("No valid AI-inferred product types in the current selection.")
        else:
            top_types, value_label = res

            top_types["llm_product_type"] = top_types["llm_product_type"].str.slice(0, 40)

            fig_type = px.bar(
                top_types.sort_values("Value", ascending=True),
                x="Value",
                y="llm_product_type",
                orientation="h",
                color_discrete_sequence=["#636EFA"],  # azul
                labels={"Value": value_label, "llm_product_type": "Product Type"},
            )

            fig_type.update_layout(
                height=480,
                margin=dict(l=10, r=10, t=10, b=10),
                showlegend=False,
            )

            fig_type.update_xaxes(tickprefix="$", separatethousands=True)

            st.plotly_chart(fig_type, use_container_width=True)

    # Marcas (colunas)
    with c2:
        st.markdown("**Top AI-Inferred Brands**")

        res = top_n(df_ai, "llm_brand_guess", n=15)

        if res is None:
            st.info("No valid AI-inferred brands in the current selection.")
        else:
            top_brands, value_label = res

            top_brands["llm_brand_guess"] = top_brands["llm_brand_guess"].str.slice(0, 40)

            fig_brand = px.bar(
                top_brands.sort_values("Value", ascending=True),
                x="Value",
                y="llm_brand_guess",
                orientation="h",
                color_discrete_sequence=["#AB63FA"],  # roxo
                labels={"Value": value_label, "llm_brand_guess": "Brand"},
            )

            fig_brand.update_layout(
                height=480,
                margin=dict(l=10, r=10, t=10, b=10),
                showlegend=False,
            )

            fig_brand.update_xaxes(tickprefix="$", separatethousands=True)

            st.plotly_chart(fig_brand, use_container_width=True)

    # Insight Estratégico (regra simples)
    st.subheader("Strategic Insight (rule-based)")

    if len(df_f) > 0:
        top_row = df_f.sort_values("units_sold_last_month", ascending=False).head(1)

        p = top_row.iloc[0]

        price = p.get("price")
        units = p.get("units_sold_last_month")
        rating = p.get("rating")
        
        name = p.get("llm_title_clean") if "llm_title_clean" in top_row.columns and pd.notna(p.get("llm_title_clean")) else p.get("product_title")

        # Tratamento seguro
        units_val = int(units) if pd.notna(units) else 0
        price_val = float(price) if pd.notna(price) else 0.0
        rating_val = float(rating) if pd.notna(rating) else None

        # Interpretação
        if rating_val is None:
            interp = "Sem avaliações suficientes para validar percepção de qualidade."
        elif rating_val >= 4.6:
            interp = "A avaliação é excelente, indicando alta satisfação e forte product–market fit."
        elif rating_val >= 4.2:
            interp = "A avaliação é muito boa, com percepção consistente de qualidade."
        elif rating_val >= 3.8:
            interp = "A avaliação é boa, com oportunidade de otimização da experiência."
        elif rating_val >= 3.3:
            interp = "A avaliação é moderada — atenção a possíveis pontos de atrito."
        else:
            interp = "A avaliação é baixa, sugerindo risco reputacional e de conversão."

        # Texto final
        rating_text = f"{rating_val:.1f} ★" if rating_val is not None else "N/A"

        st.success(
            f"### **Produto líder no recorte atual:** \n\n{name}\n\n"
            f"💰 Preço médio: **${price_val:.2f}**\n\n"
            f"📦 Volume: **{units_val:,}** un. no último mês\n\n"
            f"⭐ Rating médio: **{rating_text}**\n\n"
            f"{interp}"
        )
    else:
        st.info("Sem registros no recorte atual.")