imprimirImpares :: Int -> IO ()
imprimirImpares n = mapM_ print (impares n)

impares :: Int -> [Int]
impares 0 = []
impares n = [1, 3 .. (2 * n - 1)]

main :: IO ()
main = do
    putStrLn "Digite um número inteiro positivo:"
    nInput <- getLine
    let n = read nInput :: Int
    
    imprimirImpares n