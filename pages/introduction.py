import streamlit as st


# pylint: disable=line-too-long
def write():
    st.title('SideDL: Side-Channel Analysis with AI')

    st.header('What is SideDL?')

    st.markdown(
        'SideDL is a AI-based side-channel analysis software that provides automated and intelligent security evaluations of secure '
        'systems. SideDL provides state-of-the-art deep learning concepts for side-channel analysis.')

    st.subheader('Advantages of Deep Learning for SCA:')

    st.markdown(
        'Side-channel analysis is an active domain since 25 years ago. This field is usually divided into two main application types:')
    st.markdown('1. Direct or non-profiling attacks\n'
                '2. Two-phase or profiling attacks')
    st.markdown(
        'Examples of direct attacks are DPA and CPA methods. The most famous type of profiling attack is Template attack, which has '
        'being replaced by machine learning-based attack in the last 5 years.')

    st.markdown('Manufacturers wants to understand the level of security of their implementations with respect to different threat models. '
                'This security assessment has multiple goals:')
    st.markdown('- **Product certification** \n'
                '- **Risk assessment** \n'
                '- **Research** ')

    st.markdown(
        'To mitigate the risks posed by side-channel attacks, countermeasures are commonly added to the design. Classic attacks such'
        'as DPA, CPA or Template Attacks can be defeated with well-known countermeasures such as **hiding** or **masking**. Indeed,'
        'profiling attack, mainly Template Attacks or classic machine learning methods, are highly dependent on the feature selection'
        'phase. From the designer\'s perspective, feature selection can be prevented by adding efficient countermeasures.')

    st.markdown(
        'Thanks to the advent of powerful GPUs and availability of open-source frameworks, deep learning became a very active domain'
        'for many field, including SCA. Researchers observed that an adversary would be able to bypass countermeasures that were believed '
        'to provide sufficient security for a product. This way, deep learning showed multiple capabilities for SCA:')
    st.markdown('- Deep learning can bypass hiding and masking countermeasures when older attack methods are unable to do the same;\n'
                '- Deep learning can skip feature selection phase, which makes it a threat to different types of protections;\n'
                '- Deep learning is a highly exploratory field, where the capacity of an adversary is difficult to predict.')

    st.subheader('SideDL')

    st.markdown('SideDL software is based on three main concepts:')
    st.markdown('- **Applicability**: the software provides support for a large options of targets, including symmetric crypto algorithms, '
                'public-key cryptography implementations, lightweight ciphers and protocols.')
    st.markdown(
        '- **Optimization**: the great advantage of artificial intelligence in security evaluations is related to the automation of '
        'the analysis. For that, SideDL implements several optimization methods to find the most efficient **deep learning model** to'
        'evaluate the security of a target device.')
    st.markdown(
        '- **Explainable AI**: having a very advanced tool that can automate security evaluations is important as explain its behavior. '
        'Explainable AI is a hot trend in artificial intelligence domain able to inform the user about the decisions of algorthm. '
        'In side-channel analysis, the ExplainAI module in SideDL allows more secure implementations.')
