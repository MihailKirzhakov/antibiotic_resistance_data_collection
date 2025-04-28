# Список антибиотиков для проверки на резистентность
antibiotic_list = [
    'Penicillin', 'Oxacillin', 'Ampicillin', 'Amoxicillin',
    'Amoxicillin/Clavulanic', 'Ampicillin/Sulbactam',
    'Azlocillin', 'Carbenicillin', 'Carbenicillin-Ps', 'Ticarcillin',
    'Ticarcillin/Clavulanic', 'Mezlocillin', 'Piperacillin',
    'Piperacillin/Tazobactam', 'Imipenem', 'Meropenem',
    'Ertapenem', 'Aztreonam', 'ESβL Cft/CA', 'ESβL  Caz/CA',
    'Cephalothin', 'Cefazolin', 'Cefuroxime', 'Cefotetan',
    'Cefamandole', 'Cefoxitin', 'Cefonicid', 'Cefaclor',
    'Loracarbef', 'Cefotaxime', 'Ceftriaxone', 'Ceftizoxime',
    'Cefixime', 'Cefpodoxime', 'Cefoperazone', 'Ceftazidime',
    'Cefepime', 'Gentamicin', 'Gentamicin syn', 'Streptomyc.syn',
    'Amikacin', 'Tobramycin', 'Netilmicin', 'Spectinomycin',
    'Ciprofloxacin', 'Gatifloxacin', 'Moxifloxacin', 'Ofloxacin',
    'Lomefloxacin', 'Levofloxacin', 'Pefloxacin', 'Sparfloxacin',
    'Erytromycin', 'Clarithromycin', 'Azithromycin', 'Clindamycin',
    'Fosfomycin', 'Josamycin', 'Tetracycline', 'Minocycline',
    'Doxiciclin', 'Trimethoprim-Sulphamethoxazole',
    'Chloramphenicol', 'Rifampicin',
    'Vancomycin', 'Linezolid', 'Synercid', 'Tigecycline',
    'Daptomicin', 'Metronidazol', 'Norfloxacin', 'Cinoxacin',
    'Nalidixic Acid', 'Nitrofurantoin', 'Sulfamethoxazole', 'Trimethoprim',
    '5-НОК', 'Voriconazol', 'Amphotericin B', 'Miconazol',
    'Ketoconazole', 'Itraconazole', 'Fluconazole'
]

UNIQUE_PREFIXES_LIST = [
    # Methicillin-resistant Staphylococcus aureus
    # Метициллинрезистентные золотистые стафилококки
    {
        'prefix': ' MRSA',
        'cultures': ['Staphylococcus aureus'],
        'resistant_ab': [
            'Moxifloxacin', 'Erytromycin', 'Clindamycin', 'Ciprofloxacin'
        ]
    },
    # Extended Spectrum Betalactamas
    # Бета-лактамазы расширенного спектра действия
    {
        'prefix': ' ESBL',
        'cultures': [
            'Escherichia coli', 'Klebsiella aerogenes', 'Klebsiella pneumoniae',
            'Proteus mirabilis', 'Enterobacter cloacae', 'Citrobacter freundii',
            'Enterobacter asburiae'
        ],
        'resistant_ab': [
            'Ampicillin', 'Amoxicillin/Clavulanic', 'Cefotaxime',
            'Ceftazidime', 'Cefepime'
        ]
    },
    # Carbapenem-resistance Enterobacteriaceae
    # Карбопенем-устойчивые энтеробактерии
    {
        'prefix': ' CRE',
        'cultures': ['Klebsiella pneumoniae', 'Klebsiella oxytoca'],
        'resistant_ab': ['Imipenem', 'Meropenem', 'Cefepime']
    }
]
