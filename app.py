import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config("Climate Change")
st.title("Coastal Risk Screening")
st.subheader("Data models from Climate Central")
st.write("A comparative application showing areas threatened by sea level rise and coastal flooding. Combining the most advanced global model from Climate Central of coastal elevations with the latest projections for future flood levels")

st.markdown("### Singapore")
image_comparison(
    img1="Singapore2022.jpg",
    img2="Singapore2030.jpg",
    label1="2022",
    label2="2030",
)

st.markdown("### Bangladesh")
image_comparison(
    img1="Bangladesh2022.jpg",
    img2="Bangladesh2030.jpg",
    label1="2022",
    label2="2030",
)


st.markdown("### Malaysia")
image_comparison(
    img1="Malaysia2022.jpg",
    img2="Malaysia2030.jpg",
    label1="2022",
    label2="2030",
)

st.markdown("### Thailand")
image_comparison(
    img1="Thailand2022.jpg",
    img2="Thailand2030.jpg",
    label1="2022",
    label2="2030",
)

st.markdown("### Vietnam")
image_comparison(
    img1="Vietnam2022.jpg",
    img2="Vietnam2030.jpg",
    label1="2022",
    label2="2030",
)

st.markdown("### India")
image_comparison(
    img1="India2022.jpg",
    img2="India2030.jpg",
    label1="2022",
    label2="2030",
)

st.markdown("### China")
image_comparison(
    img1="China2022.jpg",
    img2="China2030.jpg",
    label1="2022",
    label2="2030",
)

st.markdown("### Korea")
image_comparison(
    img1="Korea2022.jpg",
    img2="Korea2030.jpg",
    label1="2022",
    label2="2030",
)

st.markdown("### Japan")
image_comparison(
    img1="Japan2022.jpg",
    img2="Japan2030.jpg",
    label1="2022",
    label2="2030",
)

st.markdown("### Brunei")
image_comparison(
    img1="Brunei2022.jpg",
    img2="Brunei2030.jpg",
    label1="2022",
    label2="2030",
)

st.markdown("### Srilanka")
image_comparison(
    img1="Srilanka2022.jpg",
    img2="Srilanka2030.jpg",
    label1="2022",
    label2="2030",
)


st.write('For more information can use Climate Central coastal portal [link](https://coastal.climatecentral.org/map/10/88.4794/22.5674/?theme=sea_level_rise&map_type=year&basemap=roadmap&contiguous=true&elevation_model=best_available&forecast_year=2030&pathway=ssp1rcp26&percentile=p50&refresh=true&return_level=return_level_1&rl_model=gtsr&slr_model=ipcc_2021_med)')
