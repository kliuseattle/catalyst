import streamlit as st 
import pandas as pd 
import random 

st.set_page_config(page_title='CatalystFeatureExplore', layout='wide')
st.header('Make inferencing on new catalysts.')
st.markdown("> 01/02/2023")


regular_dopants = ["Regular dopants", 
    "ReO4, WO4, SO4, KNO3, KOH, LiOH, CsOH, LiNO3"
]

add_on_dopants = [
    "Add-on dopants", "NaNO3, RbNO3, LiReO4, NH4F, KCL, Mo, Se, LiF, Ca(NO3)2, Sr(NO3)2, Ba(NO3)2, (NH4)S2O3, La(NO3)3, etc."
]

dopant_df = pd.DataFrame([regular_dopants, add_on_dopants], columns=["Dopant type", "Dopants"])

st.subheader("Review on current methodology.")
# st.sidebar.markdown("Review on current methodology")

with st.expander("Raw catalyst data"):
    st.dataframe(dopant_df.assign(hack='').set_index('hack'))


features =['_ReO4', '_WO4', '_SO4', '_K', '_NO3', '_OH', '_Li', '_Cs', '_Na', '_Rb',
    '_NH4', '_Cl', '_Mo0', '_Mo7O24', '_MoO4', '_SeO4', '_SiF6', '_H', '_ZrF6', '_TiO(C2O4)2', '_C2O4',
    '_SbF6', '_SO3F', '_AlF6', '_F', '_Ca', '_Sr', '_Ba', '_S2O3', '_SO3', '_NH2', '_CS', '_EDTA', '_SiO3',
    '_TEA', '_Br', '_MnO4', '_Mn', '_Mn2+', '_HAsO4', '_Fe', '_PF6', '_DTPA', '_Yb', '_Lu', '_Al', '_Mg',
    '_La', '_TaF7', '_Cr', '_Si5O11', '_VO', '_TiF6']
current_feature_dataframe = pd.DataFrame(
    [
        ["Possible compond level feature", ", ".join(features[0:15])],
        [" ",  ", ".join(features[15:30])], 
        [" ",  ", ".join(features[30:45])], 
        [" ",  ", ".join(features[45:])], 

    ], columns=["Feature type", "Features"]
)


with st.expander("Feature for the current model"):
    st.dataframe(current_feature_dataframe.assign(hack='').set_index('hack'))


with st.expander("An example with potential problems"):
    st_train, st_inference = st.columns(2)
    with st_train:
        st.write("Training experiments are conducted only with limited varieties of dopants (e.g. Mg(NO3)2, \
            ReO4, KNO3).")
        MgNO3 = [random.uniform(1,2) for _ in range(10)]
        ReO4 = [random.uniform(1,2) for _ in range(10)]
        KNO3 = [random.uniform(1,2) for _ in range(10)]

        pEO = [random.uniform(1,10) for _ in range(10)]
        Selectivity = [random.uniform(80, 99) for _ in range(10)]
        Mg_ = MgNO3
        Re_ = ReO4 
        K_ = KNO3 
        _NO3 = [2* a + b for a, b in zip(MgNO3, KNO3)]
        Na_ = [0 for _ in range(10)]
        Ba_ = [0 for _ in range(10)]
        train_df = pd.DataFrame(
            {
                "K_": K_, 
                "Mg_": Mg_,
                "Na_": Na_, 
                "Ba_": Ba_, 
                "_NO3": _NO3, 
                "pEO": pEO, 
                "Selectivity": Selectivity
                }     
        )
        st.dataframe(train_df.assign(hack='').set_index('hack'))
    
    with st_inference:
        st.write("We want to inference on the PEO and selectivity when new dopants (NaNO3 or BaNO3) are added")
        NaNO3 = [random.uniform(1,2) for _ in range(5)]
        BaNO3 = [random.uniform(1,2) for _ in range(5)]

        Na_ = NaNO3 + [0 for _ in range(5)]
        Ba_ = [0 for _ in range(5)] + BaNO3 
        _NO3 = NaNO3 + BaNO3 

        inference_df = pd.DataFrame(
            {
                "K_": [0 for _ in range(10)], 
                "Mg_": [0 for _ in range(10)], 
                "Na_": Na_, 
                "Ba_": Ba_,                
                "_NO3": _NO3, 
                "pEO": ["?" for _ in range(10)], 
                "Selectivity": ["?" for _ in range(10)]
            }
        )
        st.dataframe(inference_df.assign(hack='').set_index('hack'))
    
single_element_col = ['_K', '_Li', '_Cs', '_Na', '_Rb', '_Cl',
'_F', '_Ca', '_Sr', '_Ba', '_Br', '_Mn', '_Fe', '_Yb', '_Lu', '_Al', '_Mg', '_La', '_Cr']
alkali_element = ['_K', '_Li', '_Cs', '_Na', '_Rb', '_Cs']
alkali_earth_element = ['_Ca', '_Sr', '_Ba', '_Mg', ]
transition_metal_element = ['_Fe', '_Cr', '_Mn']
triels_element = ['_Al']
halogens_element = ['_Cl', '_F', '_Br']
lanthanides_element = ['_Yb', '_Lu', '_La']


def get_compound_type(element):
    if element in alkali_element:
        text ='''
        Alkali metals: Shiny and soft enough to cut with a knife, \
            these metals start with lithium (Li) and end with francium (Fr).\
            They are also extremely reactive and will burst into flame or even\
            explode on contact with water, so chemists store them in oils or inert gases.\
        '''
    elif element in alkali_earth_element:
        text = '''
        Alkali earth metals: Each of these elements has two electrons \
            in its outermost energy level, which makes the alkaline earths reactive \
            enough that they're rarely found alone in nature. But they're not as reactive \
            as the alkali metals. Their chemical reactions typically occur more slowly \
            and produce less heat compared to the alkali metals.
        '''
    elif element in transition_metal_element:
        text = '''
        Transition metal element: Hard but malleable, shiny, and \
            possessing good conductivity, these elements are what you typically \
            think of when you hear the word metal. Many of the greatest hits of the \
            metal world — including gold, silver, iron and platinum — live here.
        '''
    elif element in lanthanides_element:
        text = '''
        Lanthanides element: The elements in this group have a silvery white color \
            and tarnish on contact with air.
        '''
    elif element in halogens_element:
        text = '''
        Halogens element: The halogens are quite chemically reactive and \
            tend to pair up with alkali metals to produce various types of salt. \
            The table salt in your kitchen, for example, is a marriage between \
            the alkali metal sodium and the halogen chlorine.
        '''
    elif element in triels_element:
        text = '''
        Triels element: These elements have some of the classic characteristics \
            of the transition metals, but they tend to be softer and conduct more \
            poorly than other transition metals.
        '''
    return text 


property_df = pd.read_csv("properties.csv")
property_df.MolecularFormula = property_df.MolecularFormula.apply(lambda x: x.strip('-'))


with st.expander("Differences between componds"):
    comp_1, comp_2 = st.columns(2)

    with comp_1:
        feature_1 = st.selectbox(
            'Chose the first element of interest', 
            single_element_col
        )
        text_1 = get_compound_type(feature_1)
        st.write(text_1)
        molecular_weight_1 = property_df[property_df.MolecularFormula == feature_1.strip('_')].MolecularWeight.tolist()[0]
        molecular_volume_1 = property_df[property_df.MolecularFormula == feature_1.strip('_')].Molar_volume.tolist()[0]
        atomic_radius_1 = property_df[property_df.MolecularFormula == feature_1.strip('_')].Atomic_radius.tolist()[0]
        feature_df_1 = pd.DataFrame(
            [   
                ['Molecular Weight', molecular_weight_1], 
                ['Molecular Volume', molecular_volume_1],
                ['Atomic radius', atomic_radius_1]
            ], columns=('Property', 'Value')
        )
        st.dataframe(feature_df_1.assign(hack='').set_index('hack'))

    with comp_2:
        feature_2 = st.selectbox(
            'Chose the second element of interest', 
            single_element_col
        )
        text_2 = get_compound_type(feature_2)
        st.write(text_2)
        molecular_weight_2 = property_df[property_df.MolecularFormula == feature_2.strip('_')].MolecularWeight.tolist()[0]
        molecular_volume_2 = property_df[property_df.MolecularFormula == feature_2.strip('_')].Molar_volume.tolist()[0]
        atomic_radius_2 = property_df[property_df.MolecularFormula == feature_2.strip('_')].Atomic_radius.tolist()[0]
        feature_df_2 = pd.DataFrame(
            [   
                ['Molecular Weight', molecular_weight_2], 
                ['Molecular Volume', molecular_volume_2],
                ['Atomic radius', atomic_radius_2]
            ], columns=('Property', 'Value')
        )
        st.dataframe(feature_df_2.assign(hack='').set_index('hack'))

st.subheader("Develop new features for better inference")
alkali_element_cleaned = [elem.strip('_') for elem in alkali_element]
alkali_df = property_df[property_df.MolecularFormula.isin(alkali_element_cleaned)]

alkali_earth_element_cleaned = [elem.strip('_') for elem in alkali_earth_element]
alkali_earth_df = property_df[property_df.MolecularFormula.isin(alkali_earth_element_cleaned)]

transition_metal_element_cleaned = [elem.strip('_') for elem in transition_metal_element ]
transition_metal_df =  property_df[property_df.MolecularFormula.isin(transition_metal_element_cleaned)]

triels_element_cleaned = ['Al']
triels_df = property_df[property_df.MolecularFormula.isin(triels_element_cleaned)]

halogens_element_cleaned = [elem.strip('_') for elem in halogens_element]
halogens_df = property_df[property_df.MolecularFormula.isin(halogens_element_cleaned)]

lanthanides_element_cleaned = ['Yb', 'Lu', 'La']
lanthanides_df = property_df[property_df.MolecularFormula.isin(lanthanides_element_cleaned)]


with st.expander('Step 1: Categorize features into groups'):
    m1, m2, m3 = st.columns(3)
    with m1:
        st.write("Alkali metal")
        st.dataframe(alkali_df.iloc[:, 1:].assign(hack='').set_index('hack'))
    with m2:
        st.write("Alkali earth metal")
        st.dataframe(alkali_earth_df.iloc[:, 1:].assign(hack='').set_index('hack'))
    with m3:
        st.write("Transition metal")
        st.dataframe(transition_metal_df.iloc[:, 1:].assign(hack='').set_index('hack'))
    m4, m5, m6 = st.columns(3)
    with m4:
        st.write("Triels")
        st.dataframe(triels_df.iloc[:, 1:].assign(hack='').set_index('hack'))
    with m5:
        st.write("Halogens")
        st.dataframe(halogens_df.iloc[:, 1:].assign(hack='').set_index('hack'))
    with m6:
        st.write("Lanthanides")
        st.dataframe(lanthanides_df.iloc[:, 1:].assign(hack='').set_index('hack'))

with st.expander('Step 2: Compute new features'):
    st.write("We use Alkali metal as an example")
    st.write('Mass weight is the sum of all the Alkali metal mass.')
    st.write('Weighted average molecular weight is the weighted average of the molecular weight over all \
        the Alkali metals.')
    st.write('Weighted average molar volume is the weighed average of the molar value over all the \
        Alkali metals.')
    st.write('Weighted average atomic radius is the weighed average of the atomic radius over all the \
        Alkaili metals')

with st.expander("Previous example"):
    train_1, train_2 = st.columns([3,7])
    with train_1:
        st.markdown('Training data example')
        st.dataframe(train_df.assign(hack='').set_index('hack'))
    with train_2:
        st.markdown('Refactorized training data')
        alkali_mass_train = train_df.K_
        alkali_molecular_weight_train = [39.0983 for _ in range(10)]
        alkali_molecular_volume_train = [45.94 for _ in range(10)]
        alkali_atomic_radius_train = [220 for _ in range(10)]

        alkali_earth_mass_train = train_df.Mg_
        alkali_earth_molecular_weight_train = [24.3050 for _ in range(10)]
        alkali_earth_molecular_volume_train = [14 for _ in range(10)]
        alkali_earth_atomic_radius_train = [150 for _ in range(10)]
        train_df_2 = pd.DataFrame(
            {
                "Alkali mass": alkali_mass_train,
                "Alkali molecular weight": alkali_molecular_weight_train,
                "Alkali molecular volume": alkali_molecular_volume_train,
                "Alkali atomic radius": alkali_atomic_radius_train,
                "Alkali earth mass": alkali_earth_mass_train,
                "Alkali earth molecular weight": alkali_earth_molecular_weight_train,
                "Alkali earth molecular volume": alkali_earth_molecular_volume_train,
                "Alkali earth atomic radius": alkali_earth_atomic_radius_train,
                "_NO3": train_df._NO3, 
                "pEO": train_df.pEO, 
                "Selectivity": train_df.Selectivity
                }     
        )
        st.dataframe(train_df_2.assign(hack='').set_index('hack'))
    
    infer_1, infer_2 = st.columns([3,7])
    with infer_1:
        st.markdown('Experiment inference data')
        st.dataframe(inference_df.assign(hack='').set_index('hack'))
    with infer_2:
        st.markdown('Refactorized inference data')
        alkali_mass_infer = inference_df.Na_
        alkali_molecular_weight_infer = [22.9898 for _ in range(5)] + [0 for _ in range(5)]
        alkali_molecular_volume_infer = [23.78 for _ in range(5)] + [0 for _ in range(5)]
        alkali_atomic_radius_infer = [180 for _ in range(5)] + [0 for _ in range(5)]

        alkali_earth_mass_infer = inference_df.Ba_
        alkali_earth_molecular_weight_infer = [0 for _ in range(5)] + [137.33 for _ in range(5)]
        alkali_earth_molecular_volume_infer = [0 for _ in range(5)] + [38.16 for _ in range(5)]
        alkali_earth_atomic_radius_infer = [0 for _ in range(5)] + [215 for _ in range(5)]
        infer_df_2 = pd.DataFrame(
            {
                "Alkali mass": alkali_mass_infer,
                "Alkali molecular weight": alkali_molecular_weight_infer,
                "Alkali molecular volume": alkali_molecular_volume_infer,
                "Alkali atomic radius": alkali_atomic_radius_infer,
                "Alkali earth mass": alkali_earth_mass_infer,
                "Alkali earth molecular weight": alkali_earth_molecular_weight_infer,
                "Alkali earth molecular volume": alkali_earth_molecular_volume_infer,
                "Alkali earth atomic radius": alkali_earth_atomic_radius_infer,
                "_NO3": inference_df._NO3, 
                "pEO": inference_df.pEO, 
                "Selectivity": inference_df.Selectivity
                }     
        )
        st.dataframe(infer_df_2.assign(hack='').set_index('hack'))

st.subheader('Results')
st.write("Reduce 53 compond level features to 32 and maintain the same level of model performance.")
select_res = pd.read_csv('result_selectivity.csv')
pEO_res = pd.read_csv('result_PEO.csv')
with st.expander("Model performance"):
    selected_ids = st.multiselect('Select a carrier id', select_res.id.unique())
    #if len(selected_ids) == 1:
    # res_df_1 = pd.DataFrame(
    #     {
    #         'R2 selectivity (previous)': select_res[(select_res.id.isin(selected_ids)) & (select_res.type=='old')].value.tolist(),
    #         'R2 selectivity (proposed)': select_res[(select_res.id.isin(selected_ids)) & (select_res.type=='new')].value.tolist(),
    #         'R2 pEO (previous)': pEO_res[(pEO_res.id.isin(selected_ids)) & (pEO_res.type=='old')].value.tolist(),
    #         'R2 pEO (proposed)': pEO_res[(pEO_res.id.isin(selected_ids)) & (pEO_res.type=='new')].value.tolist()
    #     }
    # )
    # st.dataframe(res_df_1.assign(hack='').set_index('hack'))

    select, pEO = st.columns(2)
    with select:
        st.write('R2 for selectivity')
        res_df_select = pd.DataFrame(
            {
                'Previous method': select_res[(select_res.id.isin(selected_ids)) & (select_res.type=='old')].value.tolist(),
                'Proposed method': select_res[(select_res.id.isin(selected_ids)) & (select_res.type=='new')].value.tolist(),
            }
        )
        st.dataframe(res_df_select.assign(hack='').set_index('hack'))

    with pEO:
        st.write('R2 for pEO')
        res_df_pEO = pd.DataFrame(
            {
            'Previous method': pEO_res[(pEO_res.id.isin(selected_ids)) & (pEO_res.type=='old')].value.tolist(),
            'Proposed method': pEO_res[(pEO_res.id.isin(selected_ids)) & (pEO_res.type=='new')].value.tolist()
            }
        )
        st.dataframe(res_df_pEO.assign(hack='').set_index('hack'))
# import seaborn as sns 
# sns.catplot(x='id', y = 'value', hue='type', data = df_select, kind='bar')

st.subheader("Future work")
with st.expander("Work items"):
    st.write("1. Categorize the rest 32 compond level features into meaningful groups, e.g. oxide classification (MoO4, \
        SeO4, C2O4, etc..), fluoride classification (TiF6, TaF7 PF6, etc..), etc..")
    st.write("2. There are still unknown compound elements need further explanations (TEA and EDTA).") 
    st.write("3. Test model on other ML models such as neural network, boosting trees, etc..")
    st.write("4. Construct new training and testing strategy to test the model performance rather than random spliting.")
