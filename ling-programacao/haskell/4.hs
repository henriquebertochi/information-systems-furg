fahrenheitParaCelsius :: Double -> Double
fahrenheitParaCelsius f = (f - 32) * 5 / 9

main :: IO ()
main = do
    putStrLn "Digite a temperatura em Fahrenheit:"
    fInput <- getLine
    let f = read fInput :: Double
    
    let c = fahrenheitParaCelsius f
    
    putStrLn ("A temperatura em Celsius é: " ++ show c)