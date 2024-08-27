numPrimo :: Int -> Int -> Bool
numPrimo n d
    | n < 2 = False
    | d * d > n = True
    | n `mod` d == 0 = False
    | otherwise = auxPrimo n (d + 1)

main :: IO ()
main = do
    putStrLn "Digite um número inteiro positivo:"
    nInput <- getLine
    let n = read nInput :: Int

    if numPrimo n 2
        then putStrLn (show n ++ " é um número primo.")
        else putStrLn (show n ++ " não é um número primo.")