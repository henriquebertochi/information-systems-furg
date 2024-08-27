main :: IO ()
main = do
    putStrLn "Digite o valor de x:"
    xInput <- getLine
    let x = read xInput :: Int
    
    putStrLn "Digite o valor de n (não-negativo):"
    nInput <- getLine
    let n = read nInput :: Int
    
    let resultado = x ^ n
    
    putStrLn ("O resultado de " ++ show x ++ "^" ++ show n ++ " é: " ++ show resultado)