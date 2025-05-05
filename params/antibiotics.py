# Список антибиотиков для проверки на резистентность
antibiotic_list = [
    'Penicillin', 'Ampicillin', 'Amoxicillin',
    'Amoxicillin/Clavulanic', 'Ticarcillin',
    'Ticarcillin/Clavulanic', 'Piperacillin',
    'Piperacillin/Tazobactam', 'Imipenem', 'Meropenem',
    'Aztreonam', 'Cefazolin', 'Cefuroxime', 'Cefoxitin',
    'Cefotaxime', 'Ceftriaxone', 'Cefixime', 'Ceftazidime',
    'Cefepime', 'Gentamicin', 'Amikacin', 'Tobramycin',
    'Ciprofloxacin', 'Moxifloxacin', 'Levofloxacin',
    'Erytromycin', 'Clarithromycin', 'Azithromycin', 'Clindamycin',
    'Fosfomycin', 'Tetracycline', 'Minocycline',
    'Doxiciclin', 'Trimethoprim-Sulphamethoxazole',
    'Chloramphenicol', 'Rifampicin',
    'Vancomycin', 'Linezolid', 'Tigecycline',
    'Daptomicin', 'Norfloxacin', 'Nitrofurantoin',
    'Voriconazol', 'Amphotericin B', 'Miconazol',
    'Ketoconazole', 'Itraconazole', 'Fluconazole'
]

CR_ESBLS_CULTURES = [
    'Achromobacter xylosoxidans', 'Achromobacter xylosoxidans subsp denitrificans',
    'Acinetobacter baumannii', 'Acinetobacter pittii', 'Acinetobacter radioresistens',
    'Alcaligenes faecalis', 'Burkholderia cepacia', 'Citrobacter braakii',
    'Citrobacter freundii', 'Citrobacter koseri', 'Citrobacter koseri (diversus)',
    'Enterobacter asburiae', 'Enterobacter cloacae', 'Enterobacter hormaechei',
    'Enterobacter kobei', 'Enterobacter ludwigii', 'Escherichia coli',
    'Klebsiella aerogenes', 'Klebsiella pneumoniae', 'Klebsiella oxytoca',
    'Klebsiella variicola', 'Morganella morganii', 'Pasteurella multocida',
    'Proteus hauseri', 'Proteus mirabilis', 'Proteus vulgaris',
    'Pseudomonas aeruginosa', 'Pseudomonas fluorescens', 'Pseudomonas gessardii',
    'Pseudomonas monteilii', 'Pseudomonas putida', 'Pseudomonas stutzeri',
    'Raoultella ornithinolytica', 'Serratia liquefaciens', 'Serratia marcescens',
    'Serratia odorifera'
]

UNIQUE_PREFIXES_LIST = [
    # Methicillin-resistant Staphylococcus aureus
    # Метициллинрезистентные золотистые стафилококки
    {
        'prefix': ' MRSA',
        'cultures': ['Staphylococcus aureus'],
        'resistant_ab': ['Cefoxitin']
    },
    # Extended Spectrum Betalactamas
    # Бета-лактамазы расширенного спектра действия
    {
        'prefix': ' ESBL',
        'cultures': CR_ESBLS_CULTURES,
        'resistant_ab': ['Cefotaxime', 'Ceftazidime', 'Cefepime', 'Ceftriaxone']
    },
    # Carbapenem-resistance Enterobacteriaceae
    # Карбопенем-устойчивые энтеробактерии
    {
        'prefix': ' CR',
        'cultures': CR_ESBLS_CULTURES,
        'resistant_ab': ['Imipenem', 'Meropenem']
    }
]
