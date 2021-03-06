//+------------------------------------------------------------------+
//|                                                      ProjectName |
//|                                      Copyright 2018, CompanyName |
//|                                       http://www.companyname.net |
//+------------------------------------------------------------------+
#property copyright "Copyright 2021, MetaQuotes Software Corp."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property strict

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
int OnInit()
  {return(INIT_SUCCEEDED);}

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {}

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void OnTick()
  {
//変数の宣言
   int cnt;
   int cross_5m_BorS = 0;
   int cross_15m_BorS = 0;
   int CurrentPosition = -1;
   double old_5m_sma105,old_5m_sma315,old_15m_sma105,old_15m_sma315;
   double now_5m_sma105,now_5m_sma315,now_5m_sma105,now_15m_sma315;
   int ticket;
   int order_select;
   bool order_close;

// オーダーチェック（ポジションなどのデータ）
   for(cnt=0; cnt<OrdersTotal(); cnt++)
     {
      order_select = OrderSelect(cnt,SELECT_BY_POS);
      if(OrderSymbol() == Symbol())
        {
         CurrentPosition=cnt;
        }
     }

//一つ前の５分足,105日線
   old_5m_sma105 = iMA(NULL,PERIOD_M5,105,0,MODE_SMA,PRICE_CLOSE,1);
//一つ前の５分足,315日線
   old_5m_sma315 = iMA(NULL,PERIOD_M5,315,0,MODE_SMA,PRICE_CLOSE,1);
//一つ前の1５分足,105日線
   old_15m_sma105 = iMA(NULL,PERIOD_M15,105,0,MODE_SMA,PRICE_CLOSE,1);
//一つ前の1５分足,315日線
   old_15m_sma315 = iMA(NULL,PERIOD_M15,315,0,MODE_SMA,PRICE_CLOSE,1);

//現在の５分足,105日線
   now_5m_sma105 = iMA(NULL,PERIOD_M5,105,0,MODE_SMA,PRICE_CLOSE,0);
//現在の５分足,315日線
   now_5m_sma315 = iMA(NULL,PERIOD_M5,315,0,MODE_SMA,PRICE_CLOSE,0);
//現在の1５分足,105日線
   now_15m_sma105 = iMA(NULL,PERIOD_M15,105,0,MODE_SMA,PRICE_CLOSE,0);
//現在の1５分足,315日線
   now_15m_sma315 = iMA(NULL,PERIOD_M15,315,0,MODE_SMA,PRICE_CLOSE,0);


// ポジションチェック　ポジション無し
   if(CurrentPosition == -1)
     {
      // 15分足のゴールデンクロス
      if(old_15m_sma105 < old_15m_sma315 && now_15m_sma105 >= now_15m_sma315)
        {
          cross_15m_BorS = 1
        }
      }
      // 15分足デッドクロス
      if(old_15m_sma105 > old_15m_sma315 && now_15m_sma105 <= now_15m_sma315)
        {
          cross_15m_BorS = -1
        }
      }
      
      // 5分足のゴールデンクロス
      if(old_5m_sma105 < old_5m_sma315 && now_5m_sma105 >= now_5m_sma315)
        {
          cross_5m_BorS = 1
        }
      }
      // 5分足のデッドクロス
      if(old_5m_sma105 > old_5m_sma315 && now_5m_sma105 <= now_5m_sma315)
        {
          cross_5m_BorS = -1
        }
      }

// ポジション有り

   else

     {

      //ポジションの選択

      order_select = OrderSelect(CurrentPosition,SELECT_BY_POS);



      //ポジションの確認

      if(OrderSymbol() == Symbol())

        {

         //もし買いポジションだったら

         if(OrderType()==OP_BUY)

           {

            //もし２１日線が９０日線を上から下にクロスしたら

            if(old_5m_sma105 > old_5m_sma315 && now_5m_sma105 <= now_5m_sma315)

              {

               //手仕舞い

               order_close = OrderClose(OrderTicket(),OrderLots(),Bid,30,Green);

              }

           }

        }

     }



  }

//+------------------------------------------------------------------+

//+------------------------------------------------------------------+


         //買いポジションを持つ

         ticket = OrderSend(Symbol(), OP_BUY, 0.1, Ask, 30, 0,0, "Buy", 0, 0, clrBlue);