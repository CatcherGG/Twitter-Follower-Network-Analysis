AnalyzeNetworkNotebook
================
GuyGo and Ofri Masad

Network Analysis:
=================

### Reading the data

The data is a csv files containing the graph edges of my twitter followers. And edge is represented by couple: {From, To}

``` r
head(ga.data)
```

    ##            From    To
    ## 1      areldoga 1996E
    ## 2      ImahAbah 1996E
    ## 3  ItayShoshani 1996E
    ## 4      papering 1996E
    ## 5     orkoren34 1996E
    ## 6 MattiSvatizky 1996E

### Data exploration:

#### Followers:

We've fetched information from CatcherGG\[Guy Gonen\] and his 134 followers. For each follower we fetched up to 200 possible followers and then dropped people which are not following CatcherGG \[In order to not exceed 200 nodes\].

``` r
V(g)$name
```

    ##   [1] "areldoga"        "ImahAbah"        "ItayShoshani"   
    ##   [4] "papering"        "orkoren34"       "MattiSvatizky"  
    ##   [7] "yberrypot"       "Nitzan_bi"       "IParohod"       
    ##  [10] "lBenua"          "Cat_Blog"        "PcGunMan"       
    ##  [13] "1996E"           "fluffyguy"       "myradiocoil"    
    ##  [16] "HerrNadav"       "TallyMa1"        "NettaBeiton"    
    ##  [19] "krembo296"       "Teo_Galvan"      "DanDilll"       
    ##  [22] "Avshalom_eitan"  "BoazAri"         "Catmoviesnet"   
    ##  [25] "HatulZoef"       "rahelik5"        "Israel_Coaching"
    ##  [28] "Palavragame"     "GraphyNess"      "honeysin42"     
    ##  [31] "favstar_bot102"  "mmmmichal"       "Metalit123"     
    ##  [34] "301183"          "naknikim"        "PaRaDoX_LaDy"   
    ##  [37] "shaulhayun"      "shira_chen_"     "revetalosh"     
    ##  [40] "EliranTamsuT"    "ShovalBitton"    "sapirAsh"       
    ##  [43] "DimaSurikov"     "shakedbu"        "HaiTanami"      
    ##  [46] "talkaza"         "BambaBoba"       "DaveClub"       
    ##  [49] "4Trillian"       "balariv"         "SofiZach"       
    ##  [52] "RoeiR"           "AmirOz"          "Mimoola21"      
    ##  [55] "SinayaShemesh"   "Vinethropy"      "funnycatstub"   
    ##  [58] "michalidan13"    "shanigu1"        "yosi25111"      
    ##  [61] "MizrRene"        "amihaialfon"     "barakshalev"    
    ##  [64] "Yarden_BY"       "932_54"          "doronily"       
    ##  [67] "BikLihi"         "Rose_ShaMimie"   "IvgiH"          
    ##  [70] "yoav1982b"       "Duckinyu"        "TShagrir"       
    ##  [73] "ItaiSanders"     "vered457"        "ofersagi"       
    ##  [76] "TomerSaban"      "MilProvencio"    "AlenaJany"      
    ##  [79] "YalondaRomer"    "romantif1"       "The_Asss"       
    ##  [82] "liranohali"      "lidanh"          "CohenRan"       
    ##  [85] "OrianZinger"     "yali3ma"         "_SoyCD"         
    ##  [88] "ShafirYael"      "zebrale"         "rafaelBenMuha"  
    ##  [91] "shirley__h"      "GreatKubani"     "meiravashoush"  
    ##  [94] "Shiranumn"       "talmaXO"         "The_RadRabbit"  
    ##  [97] "YHWH_Adonai"     "gavri33"         "BlueEyes0_0"    
    ## [100] "that_is_a_no"    "daniel66321302"  "elmlak"         
    ## [103] "Crystalyani"     "bemileil"        "sagiangel"      
    ## [106] "MabsooTahat"     "sh00shka"        "whileLooper"    
    ## [109] "natan12131"      "ismystore"       "Shalvatta"      
    ## [112] "MikeSchism"      "shaybut"         "tokbekist"      
    ## [115] "yogigueta"       "nerya_elul"      "NirOvadia"      
    ## [118] "BitcoinIL"       "TALYLAVY"        "Would_you83"    
    ## [121] "hymerus"         "inbarm92"        "natan0044"      
    ## [124] "Long_Username"   "KimDashIAm"      "WilliamRodgers" 
    ## [127] "KingozaurBot1"   "spesSelene"      "Blondinie_boy"  
    ## [130] "yehudasherro"    "Shahaf1410"      "polinaraf1"     
    ## [133] "MoradMuslimany"  "eldars1990"      "CatcherGG"

#### Number of Connections between followers and followers of followers:

``` r
summary(g)
```

    ## IGRAPH UN-- 135 1363 -- 
    ## + attr: name (v/c)

### Data-visualization:

#### Basic representation:

``` r
g$layout <- layout.fruchterman.reingold(g)
plot(g)
```

![](AnalyzeNetworkNotebook_files/figure-markdown_github/basic-1.png)<!-- --> \#\#\#\# Basic representation without names \[We'll continue without names from now on\]:

``` r
V(g)$label <- NA 
g$layout <- layout.fruchterman.reingold(g)
plot(g)
```

![](AnalyzeNetworkNotebook_files/figure-markdown_github/basic_rep2-1.png)<!-- -->

#### Degree score:

``` r
degr.score <- degree(g)
degr.score
```

    ##        areldoga        ImahAbah    ItayShoshani        papering 
    ##              14              14              13              14 
    ##       orkoren34   MattiSvatizky       yberrypot       Nitzan_bi 
    ##              14              14              14              14 
    ##        IParohod          lBenua        Cat_Blog        PcGunMan 
    ##              14              13              14              14 
    ##           1996E       fluffyguy     myradiocoil       HerrNadav 
    ##              14              14              20              20 
    ##        TallyMa1     NettaBeiton       krembo296      Teo_Galvan 
    ##              20              20              20              20 
    ##        DanDilll  Avshalom_eitan         BoazAri    Catmoviesnet 
    ##              20              20              20              20 
    ##       HatulZoef        rahelik5 Israel_Coaching     Palavragame 
    ##              20              20              20              20 
    ##      GraphyNess      honeysin42  favstar_bot102       mmmmichal 
    ##              20              20              20              20 
    ##      Metalit123          301183        naknikim    PaRaDoX_LaDy 
    ##              20              20              20              20 
    ##      shaulhayun     shira_chen_      revetalosh    EliranTamsuT 
    ##              20              20              20              20 
    ##    ShovalBitton        sapirAsh     DimaSurikov        shakedbu 
    ##              20              20              20              20 
    ##       HaiTanami         talkaza       BambaBoba        DaveClub 
    ##              20              20              20              20 
    ##       4Trillian         balariv        SofiZach           RoeiR 
    ##              20              20              20              20 
    ##          AmirOz       Mimoola21   SinayaShemesh      Vinethropy 
    ##              20              20              20              20 
    ##    funnycatstub    michalidan13        shanigu1       yosi25111 
    ##              20              20              20              20 
    ##        MizrRene     amihaialfon     barakshalev       Yarden_BY 
    ##              20              20              20              20 
    ##          932_54        doronily         BikLihi   Rose_ShaMimie 
    ##              20              20              20              20 
    ##           IvgiH       yoav1982b        Duckinyu        TShagrir 
    ##              20              20              20              20 
    ##     ItaiSanders        vered457        ofersagi      TomerSaban 
    ##              20              20              19              20 
    ##    MilProvencio       AlenaJany    YalondaRomer       romantif1 
    ##              20              20              20              20 
    ##        The_Asss      liranohali          lidanh        CohenRan 
    ##              20              20              20              20 
    ##     OrianZinger         yali3ma          _SoyCD      ShafirYael 
    ##              20              20              20              20 
    ##         zebrale   rafaelBenMuha      shirley__h     GreatKubani 
    ##              20              19              20              20 
    ##   meiravashoush       Shiranumn         talmaXO   The_RadRabbit 
    ##              20              20              20              20 
    ##     YHWH_Adonai         gavri33     BlueEyes0_0    that_is_a_no 
    ##              20              20              20              20 
    ##  daniel66321302          elmlak     Crystalyani        bemileil 
    ##              20              20              20              20 
    ##       sagiangel     MabsooTahat        sh00shka     whileLooper 
    ##              20              20              20              20 
    ##      natan12131       ismystore       Shalvatta      MikeSchism 
    ##              20              20              20              20 
    ##         shaybut       tokbekist       yogigueta      nerya_elul 
    ##              20              20              20              20 
    ##       NirOvadia       BitcoinIL        TALYLAVY     Would_you83 
    ##              20              20              20              20 
    ##         hymerus        inbarm92       natan0044   Long_Username 
    ##              20              20              20              20 
    ##      KimDashIAm  WilliamRodgers   KingozaurBot1      spesSelene 
    ##              20              20              20              20 
    ##   Blondinie_boy    yehudasherro      Shahaf1410      polinaraf1 
    ##              20              20              20              20 
    ##  MoradMuslimany      eldars1990       CatcherGG 
    ##              20              20             134

``` r
V(g)$size <- degree(g) * 0.4 # multiply by 2 for scale 
plot(g)
```

![](AnalyzeNetworkNotebook_files/figure-markdown_github/degree-1.png)<!-- -->

#### Closeness centrality:

``` r
clo <- closeness(g) 
# rescale values to match the elements of a color vector 
clo.score <- round( (clo - min(clo)) * length(clo) / max(clo) ) + 1 
# create color vector, use rev to make red "hot" 
clo.colors <- rev(heat.colors(max(clo.score))) 
V(g)$color <- clo.colors[ clo.score ] 
plot(g)
```

![](AnalyzeNetworkNotebook_files/figure-markdown_github/closeness_cent-1.png)<!-- -->

#### Betweeness centrality.

``` r
btw <- betweenness(g) 
btw.score <- round(btw) + 1 
btw.colors <- rev(heat.colors(max(btw.score))) 
V(g)$color <- btw.colors[ btw.score ] 
plot(g)
```

![](AnalyzeNetworkNotebook_files/figure-markdown_github/betweeness_cent-1.png)<!-- -->

### Insights:

1.  There are 7 disjoint cliques. When taking a closer look at the people in each cliques it was possible to easily tag them: University, Army, English twitter persons, ...
2.  It wasn't a suprise that CatcherGG would be in the middle since we know that everyone follows him.
3.  There is one clique which is made of people that almost has no followers, And they are connected with themselves and a few others. Some of them are bots and some of them are new people that are not active this days.
