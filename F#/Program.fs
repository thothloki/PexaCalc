// Learn more about F# at http://fsharp.org

open System
open FSharp.Data
open Newtonsoft.Json

let marketDetailJson = Http.RequestString( "https://api.freiexchange.com/public/ticker/PEXA", httpMethod="GET" )

type MarketDetail =
  {
    marketId: int
    volume24h: float
    average24h: float
    high: float
    low: float
    last: float
    highestBuy: float
    lowestSell: float
    volume24h_btc: float
    percent_change_24h: float
  }

let detailMap = JsonConvert.DeserializeObject<Map<string, MarketDetail array>>(marketDetailJson)

detailMap.["PEXA_BTC"]
|> Seq.map (fun detail -> detail.low)
|> Seq.iter (fun low -> printfn "%.8f" low)

let low = detailMap.["PEXA_BTC"].[0].low
let high = detailMap.["PEXA_BTC"].[0].high
let last = detailMap.["PEXA_BTC"].[0].last

//printfn "Low is %.8f" low
//printfn "High is %.8f" high
//printfn "Last sale sold for %.8f" last

printf "How many pexa do you have? "
let quantity = Console.ReadLine()

let c = quantity.AsFloat() * low
printfn "Your PEXA is worth %.8f BTC" c

printf "Press any key to exit ..."
Console.ReadKey() |> ignore