def CreateNewFeatures(df):
    df['RainEffect'] = df['RainingDays'] * df['AverageRainingDays']
    df['FruitSetMassRatio'] = df['fruitset'] / (df['fruitmass'] + 1e-5)  # Adding a small number to avoid division by zero
    df['clonesizehoneybee'] = df['clonesize'] + df['honeybee']
    #df['temp2'] = df['fruitmass'] + df['seeds']


    # Create new features
    df['TemperatureRangeUpper'] =df['MaxOfUpperTRange'] -df['MinOfUpperTRange']
    df['TemperatureRangeLower'] =df['MaxOfLowerTRange'] -df['MinOfLowerTRange']
    df['PollinatorActivity'] =df['honeybee'] +df['bumbles'] +df['andrena'] +df['osmia']
    df['FruitSeedComposite'] =df['fruitset'] *df['fruitmass'] *df['seeds']

    df['AverageTemperature'] = (df['AverageOfUpperTRange'] + df['AverageOfLowerTRange']) / 2
    df['RainAdjustedFruitMass'] = df['fruitmass'] * df['AverageRainingDays']
    df['SeedDensity'] = df['seeds'] / df['clonesize']

    return df

