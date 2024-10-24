import streamlit as st
from streamlit.components.v1 import html

# Render the chart in Streamlit using streamlit.components.v1.html
st.title("Why Toyota ?")
st.html('''
<body class="stackedit">
<h2 id="how-it-started">How it started</h2>
<p>Saudi Arabia’s automobile history is a reflection of the country’s swift economic development and modernity. Car ownership started to rise sharply once oil was discovered in the <strong>1930s</strong>, especially in the <strong>1950s</strong> when foreign brands started to compete. This growth has been fueled by important alliances, like <strong>Toyota’s</strong> regional presence.</p>
<p><strong>Toyota’s</strong> performance in Saudi Arabia is depicted in the chart below, which also shows the company’s market dominance and consumer appeal. The data provided shows how <strong>Toyota</strong> has adjusted to shifting consumer preferences over time and preserved its position as a preferred brand.</p>

''')
st.image(r"newplot.png", use_column_width=True)  # Adjust the path to your image file
st.html('''
<h2 id="a-wide-range-of-vehicles">A Wide Range of Vehicles</h2>
<p><strong>Toyota</strong> provides a wide variety of automobiles designed to satisfy the particular requirements and tastes of Saudi Arabian customers. Popular models include the <strong>Toyota Land Cruiser</strong>, which is well-known for its luxurious amenities and off-road capabilities, and the dependable <strong>Toyota Hilux</strong>, which is preferred for its longevity in commercial use.<br>
Because of its small size and fuel efficiency, <strong>the Corolla</strong> is still a popular option for city drivers. Families looking for roomy and cozy options are also catered to by the <strong>RAV4 and Camry</strong>. This wide range of models demonstrates Toyota’s dedication to provide automobiles that meet local needs, whether they be for daily commuting or tough utility.</p>
''')
st.image(r"image3.png", use_column_width=True)  # Adjust the path to your image file

st.html('''
<p>In this diverse landscape of vehicles, we find <strong>Khalid</strong>, a man living in Riyadh whose story exemplifies the Toyota experience. After an unfortunate accident crushed his beloved Corolla, Khalid faced the challenge of finding a reliable replacement. With a family to support and a tight budget, he turned to the used car market.</p>
<p><strong>Khalid</strong> was taken aback by the sheer number of options at the Sayarah dealership. While he was drawn to Toyota’s reputation and quality, he couldn’t help but compare prices from a chart he had seen, highlighting variations among different models in various locations. The differing prices left him unsure about which option offered the best value for his family’s needs. As he weighed the features and costs, he felt he needed more information to make the right choice, so he turned to the chart below for a clearer perspective.</p>
''')
st.image(r"image2.png", use_column_width=True)  # Adjust the path to your image file
st.html('''
<p>He examined the data and saw how the pricing of Toyota vehicles were affected by variables such as engine size, production year, gear type, mileage, and place of origin. He observed, for example, that older manufacturing years usually produced more reasonably priced options, whereas lesser mileage frequently resulted in higher prices. Costs were also influenced by the engine size, which affected both performance and fuel efficiency, and the kind of gear—manual versus automatic. He was able to reduce his options and have a better understanding of the market because to this thorough perspective.</p>
''')
st.image(r"image1.png", use_column_width=True)  # Adjust the path to your image file
st.html('''
<p>After carefully examining the charts and comparing the prices with his budget, <strong>Khalid</strong> began to feel more confident in his decision-making process. He realized that while newer models with lower mileage and larger engines were appealing, they often stretched his budget too far.</p>
<p>By focusing on a used <strong>Toyota</strong> Yars 2014 as it’s from a recent production year, he found a balance between affordability and quality. The data highlighted that a model with moderate mileage and a manual transmission could offer the reliability he needed without breaking the bank. With a clearer understanding of the market and a solid plan in place, <strong>Khalid</strong> felt ready to make a choice that would best serve his family’s needs while staying within his financial limits.</p>
</div>
</body>
''')
