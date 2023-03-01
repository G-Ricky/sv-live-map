"""Enum for pokemon species"""
# pylint: disable=too-many-lines

from enum import IntEnum


class Species(IntEnum):
    """Enum for pokemon species"""

    NONE = 0
    BULBASAUR = 1
    IVYSAUR = 2
    VENUSAUR = 3
    CHARMANDER = 4
    CHARMELEON = 5
    CHARIZARD = 6
    SQUIRTLE = 7
    WARTORTLE = 8
    BLASTOISE = 9
    CATERPIE = 10
    METAPOD = 11
    BUTTERFREE = 12
    WEEDLE = 13
    KAKUNA = 14
    BEEDRILL = 15
    PIDGEY = 16
    PIDGEOTTO = 17
    PIDGEOT = 18
    RATTATA = 19
    RATICATE = 20
    SPEAROW = 21
    FEAROW = 22
    EKANS = 23
    ARBOK = 24
    PIKACHU = 25
    RAICHU = 26
    SANDSHREW = 27
    SANDSLASH = 28
    NIDORAN_F = 29
    NIDORINA = 30
    NIDOQUEEN = 31
    NIDORAN_M = 32
    NIDORINO = 33
    NIDOKING = 34
    CLEFAIRY = 35
    CLEFABLE = 36
    VULPIX = 37
    NINETALES = 38
    JIGGLYPUFF = 39
    WIGGLYTUFF = 40
    ZUBAT = 41
    GOLBAT = 42
    ODDISH = 43
    GLOOM = 44
    VILEPLUME = 45
    PARAS = 46
    PARASECT = 47
    VENONAT = 48
    VENOMOTH = 49
    DIGLETT = 50
    DUGTRIO = 51
    MEOWTH = 52
    PERSIAN = 53
    PSYDUCK = 54
    GOLDUCK = 55
    MANKEY = 56
    PRIMEAPE = 57
    GROWLITHE = 58
    ARCANINE = 59
    POLIWAG = 60
    POLIWHIRL = 61
    POLIWRATH = 62
    ABRA = 63
    KADABRA = 64
    ALAKAZAM = 65
    MACHOP = 66
    MACHOKE = 67
    MACHAMP = 68
    BELLSPROUT = 69
    WEEPINBELL = 70
    VICTREEBEL = 71
    TENTACOOL = 72
    TENTACRUEL = 73
    GEODUDE = 74
    GRAVELER = 75
    GOLEM = 76
    PONYTA = 77
    RAPIDASH = 78
    SLOWPOKE = 79
    SLOWBRO = 80
    MAGNEMITE = 81
    MAGNETON = 82
    FARFETCHD = 83
    DODUO = 84
    DODRIO = 85
    SEEL = 86
    DEWGONG = 87
    GRIMER = 88
    MUK = 89
    SHELLDER = 90
    CLOYSTER = 91
    GASTLY = 92
    HAUNTER = 93
    GENGAR = 94
    ONIX = 95
    DROWZEE = 96
    HYPNO = 97
    KRABBY = 98
    KINGLER = 99
    VOLTORB = 100
    ELECTRODE = 101
    EXEGGCUTE = 102
    EXEGGUTOR = 103
    CUBONE = 104
    MAROWAK = 105
    HITMONLEE = 106
    HITMONCHAN = 107
    LICKITUNG = 108
    KOFFING = 109
    WEEZING = 110
    RHYHORN = 111
    RHYDON = 112
    CHANSEY = 113
    TANGELA = 114
    KANGASKHAN = 115
    HORSEA = 116
    SEADRA = 117
    GOLDEEN = 118
    SEAKING = 119
    STARYU = 120
    STARMIE = 121
    MR_MIME = 122
    SCYTHER = 123
    JYNX = 124
    ELECTABUZZ = 125
    MAGMAR = 126
    PINSIR = 127
    TAUROS = 128
    MAGIKARP = 129
    GYARADOS = 130
    LAPRAS = 131
    DITTO = 132
    EEVEE = 133
    VAPOREON = 134
    JOLTEON = 135
    FLAREON = 136
    PORYGON = 137
    OMANYTE = 138
    OMASTAR = 139
    KABUTO = 140
    KABUTOPS = 141
    AERODACTYL = 142
    SNORLAX = 143
    ARTICUNO = 144
    ZAPDOS = 145
    MOLTRES = 146
    DRATINI = 147
    DRAGONAIR = 148
    DRAGONITE = 149
    MEWTWO = 150
    MEW = 151
    CHIKORITA = 152
    BAYLEEF = 153
    MEGANIUM = 154
    CYNDAQUIL = 155
    QUILAVA = 156
    TYPHLOSION = 157
    TOTODILE = 158
    CROCONAW = 159
    FERALIGATR = 160
    SENTRET = 161
    FURRET = 162
    HOOTHOOT = 163
    NOCTOWL = 164
    LEDYBA = 165
    LEDIAN = 166
    SPINARAK = 167
    ARIADOS = 168
    CROBAT = 169
    CHINCHOU = 170
    LANTURN = 171
    PICHU = 172
    CLEFFA = 173
    IGGLYBUFF = 174
    TOGEPI = 175
    TOGETIC = 176
    NATU = 177
    XATU = 178
    MAREEP = 179
    FLAAFFY = 180
    AMPHAROS = 181
    BELLOSSOM = 182
    MARILL = 183
    AZUMARILL = 184
    SUDOWOODO = 185
    POLITOED = 186
    HOPPIP = 187
    SKIPLOOM = 188
    JUMPLUFF = 189
    AIPOM = 190
    SUNKERN = 191
    SUNFLORA = 192
    YANMA = 193
    WOOPER = 194
    QUAGSIRE = 195
    ESPEON = 196
    UMBREON = 197
    MURKROW = 198
    SLOWKING = 199
    MISDREAVUS = 200
    UNOWN = 201
    WOBBUFFET = 202
    GIRAFARIG = 203
    PINECO = 204
    FORRETRESS = 205
    DUNSPARCE = 206
    GLIGAR = 207
    STEELIX = 208
    SNUBBULL = 209
    GRANBULL = 210
    QWILFISH = 211
    SCIZOR = 212
    SHUCKLE = 213
    HERACROSS = 214
    SNEASEL = 215
    TEDDIURSA = 216
    URSARING = 217
    SLUGMA = 218
    MAGCARGO = 219
    SWINUB = 220
    PILOSWINE = 221
    CORSOLA = 222
    REMORAID = 223
    OCTILLERY = 224
    DELIBIRD = 225
    MANTINE = 226
    SKARMORY = 227
    HOUNDOUR = 228
    HOUNDOOM = 229
    KINGDRA = 230
    PHANPY = 231
    DONPHAN = 232
    PORYGON2 = 233
    STANTLER = 234
    SMEARGLE = 235
    TYROGUE = 236
    HITMONTOP = 237
    SMOOCHUM = 238
    ELEKID = 239
    MAGBY = 240
    MILTANK = 241
    BLISSEY = 242
    RAIKOU = 243
    ENTEI = 244
    SUICUNE = 245
    LARVITAR = 246
    PUPITAR = 247
    TYRANITAR = 248
    LUGIA = 249
    HO_OH = 250
    CELEBI = 251
    TREECKO = 252
    GROVYLE = 253
    SCEPTILE = 254
    TORCHIC = 255
    COMBUSKEN = 256
    BLAZIKEN = 257
    MUDKIP = 258
    MARSHTOMP = 259
    SWAMPERT = 260
    POOCHYENA = 261
    MIGHTYENA = 262
    ZIGZAGOON = 263
    LINOONE = 264
    WURMPLE = 265
    SILCOON = 266
    BEAUTIFLY = 267
    CASCOON = 268
    DUSTOX = 269
    LOTAD = 270
    LOMBRE = 271
    LUDICOLO = 272
    SEEDOT = 273
    NUZLEAF = 274
    SHIFTRY = 275
    TAILLOW = 276
    SWELLOW = 277
    WINGULL = 278
    PELIPPER = 279
    RALTS = 280
    KIRLIA = 281
    GARDEVOIR = 282
    SURSKIT = 283
    MASQUERAIN = 284
    SHROOMISH = 285
    BRELOOM = 286
    SLAKOTH = 287
    VIGOROTH = 288
    SLAKING = 289
    NINCADA = 290
    NINJASK = 291
    SHEDINJA = 292
    WHISMUR = 293
    LOUDRED = 294
    EXPLOUD = 295
    MAKUHITA = 296
    HARIYAMA = 297
    AZURILL = 298
    NOSEPASS = 299
    SKITTY = 300
    DELCATTY = 301
    SABLEYE = 302
    MAWILE = 303
    ARON = 304
    LAIRON = 305
    AGGRON = 306
    MEDITITE = 307
    MEDICHAM = 308
    ELECTRIKE = 309
    MANECTRIC = 310
    PLUSLE = 311
    MINUN = 312
    VOLBEAT = 313
    ILLUMISE = 314
    ROSELIA = 315
    GULPIN = 316
    SWALOT = 317
    CARVANHA = 318
    SHARPEDO = 319
    WAILMER = 320
    WAILORD = 321
    NUMEL = 322
    CAMERUPT = 323
    TORKOAL = 324
    SPOINK = 325
    GRUMPIG = 326
    SPINDA = 327
    TRAPINCH = 328
    VIBRAVA = 329
    FLYGON = 330
    CACNEA = 331
    CACTURNE = 332
    SWABLU = 333
    ALTARIA = 334
    ZANGOOSE = 335
    SEVIPER = 336
    LUNATONE = 337
    SOLROCK = 338
    BARBOACH = 339
    WHISCASH = 340
    CORPHISH = 341
    CRAWDAUNT = 342
    BALTOY = 343
    CLAYDOL = 344
    LILEEP = 345
    CRADILY = 346
    ANORITH = 347
    ARMALDO = 348
    FEEBAS = 349
    MILOTIC = 350
    CASTFORM = 351
    KECLEON = 352
    SHUPPET = 353
    BANETTE = 354
    DUSKULL = 355
    DUSCLOPS = 356
    TROPIUS = 357
    CHIMECHO = 358
    ABSOL = 359
    WYNAUT = 360
    SNORUNT = 361
    GLALIE = 362
    SPHEAL = 363
    SEALEO = 364
    WALREIN = 365
    CLAMPERL = 366
    HUNTAIL = 367
    GOREBYSS = 368
    RELICANTH = 369
    LUVDISC = 370
    BAGON = 371
    SHELGON = 372
    SALAMENCE = 373
    BELDUM = 374
    METANG = 375
    METAGROSS = 376
    REGIROCK = 377
    REGICE = 378
    REGISTEEL = 379
    LATIAS = 380
    LATIOS = 381
    KYOGRE = 382
    GROUDON = 383
    RAYQUAZA = 384
    JIRACHI = 385
    DEOXYS = 386
    TURTWIG = 387
    GROTLE = 388
    TORTERRA = 389
    CHIMCHAR = 390
    MONFERNO = 391
    INFERNAPE = 392
    PIPLUP = 393
    PRINPLUP = 394
    EMPOLEON = 395
    STARLY = 396
    STARAVIA = 397
    STARAPTOR = 398
    BIDOOF = 399
    BIBAREL = 400
    KRICKETOT = 401
    KRICKETUNE = 402
    SHINX = 403
    LUXIO = 404
    LUXRAY = 405
    BUDEW = 406
    ROSERADE = 407
    CRANIDOS = 408
    RAMPARDOS = 409
    SHIELDON = 410
    BASTIODON = 411
    BURMY = 412
    WORMADAM = 413
    MOTHIM = 414
    COMBEE = 415
    VESPIQUEN = 416
    PACHIRISU = 417
    BUIZEL = 418
    FLOATZEL = 419
    CHERUBI = 420
    CHERRIM = 421
    SHELLOS = 422
    GASTRODON = 423
    AMBIPOM = 424
    DRIFLOON = 425
    DRIFBLIM = 426
    BUNEARY = 427
    LOPUNNY = 428
    MISMAGIUS = 429
    HONCHKROW = 430
    GLAMEOW = 431
    PURUGLY = 432
    CHINGLING = 433
    STUNKY = 434
    SKUNTANK = 435
    BRONZOR = 436
    BRONZONG = 437
    BONSLY = 438
    MIME_JR = 439
    HAPPINY = 440
    CHATOT = 441
    SPIRITOMB = 442
    GIBLE = 443
    GABITE = 444
    GARCHOMP = 445
    MUNCHLAX = 446
    RIOLU = 447
    LUCARIO = 448
    HIPPOPOTAS = 449
    HIPPOWDON = 450
    SKORUPI = 451
    DRAPION = 452
    CROAGUNK = 453
    TOXICROAK = 454
    CARNIVINE = 455
    FINNEON = 456
    LUMINEON = 457
    MANTYKE = 458
    SNOVER = 459
    ABOMASNOW = 460
    WEAVILE = 461
    MAGNEZONE = 462
    LICKILICKY = 463
    RHYPERIOR = 464
    TANGROWTH = 465
    ELECTIVIRE = 466
    MAGMORTAR = 467
    TOGEKISS = 468
    YANMEGA = 469
    LEAFEON = 470
    GLACEON = 471
    GLISCOR = 472
    MAMOSWINE = 473
    PORYGON_Z = 474
    GALLADE = 475
    PROBOPASS = 476
    DUSKNOIR = 477
    FROSLASS = 478
    ROTOM = 479
    UXIE = 480
    MESPRIT = 481
    AZELF = 482
    DIALGA = 483
    PALKIA = 484
    HEATRAN = 485
    REGIGIGAS = 486
    GIRATINA = 487
    CRESSELIA = 488
    PHIONE = 489
    MANAPHY = 490
    DARKRAI = 491
    SHAYMIN = 492
    ARCEUS = 493
    VICTINI = 494
    SNIVY = 495
    SERVINE = 496
    SERPERIOR = 497
    TEPIG = 498
    PIGNITE = 499
    EMBOAR = 500
    OSHAWOTT = 501
    DEWOTT = 502
    SAMUROTT = 503
    PATRAT = 504
    WATCHOG = 505
    LILLIPUP = 506
    HERDIER = 507
    STOUTLAND = 508
    PURRLOIN = 509
    LIEPARD = 510
    PANSAGE = 511
    SIMISAGE = 512
    PANSEAR = 513
    SIMISEAR = 514
    PANPOUR = 515
    SIMIPOUR = 516
    MUNNA = 517
    MUSHARNA = 518
    PIDOVE = 519
    TRANQUILL = 520
    UNFEZANT = 521
    BLITZLE = 522
    ZEBSTRIKA = 523
    ROGGENROLA = 524
    BOLDORE = 525
    GIGALITH = 526
    WOOBAT = 527
    SWOOBAT = 528
    DRILBUR = 529
    EXCADRILL = 530
    AUDINO = 531
    TIMBURR = 532
    GURDURR = 533
    CONKELDURR = 534
    TYMPOLE = 535
    PALPITOAD = 536
    SEISMITOAD = 537
    THROH = 538
    SAWK = 539
    SEWADDLE = 540
    SWADLOON = 541
    LEAVANNY = 542
    VENIPEDE = 543
    WHIRLIPEDE = 544
    SCOLIPEDE = 545
    COTTONEE = 546
    WHIMSICOTT = 547
    PETILIL = 548
    LILLIGANT = 549
    BASCULIN = 550
    SANDILE = 551
    KROKOROK = 552
    KROOKODILE = 553
    DARUMAKA = 554
    DARMANITAN = 555
    MARACTUS = 556
    DWEBBLE = 557
    CRUSTLE = 558
    SCRAGGY = 559
    SCRAFTY = 560
    SIGILYPH = 561
    YAMASK = 562
    COFAGRIGUS = 563
    TIRTOUGA = 564
    CARRACOSTA = 565
    ARCHEN = 566
    ARCHEOPS = 567
    TRUBBISH = 568
    GARBODOR = 569
    ZORUA = 570
    ZOROARK = 571
    MINCCINO = 572
    CINCCINO = 573
    GOTHITA = 574
    GOTHORITA = 575
    GOTHITELLE = 576
    SOLOSIS = 577
    DUOSION = 578
    REUNICLUS = 579
    DUCKLETT = 580
    SWANNA = 581
    VANILLITE = 582
    VANILLISH = 583
    VANILLUXE = 584
    DEERLING = 585
    SAWSBUCK = 586
    EMOLGA = 587
    KARRABLAST = 588
    ESCAVALIER = 589
    FOONGUS = 590
    AMOONGUSS = 591
    FRILLISH = 592
    JELLICENT = 593
    ALOMOMOLA = 594
    JOLTIK = 595
    GALVANTULA = 596
    FERROSEED = 597
    FERROTHORN = 598
    KLINK = 599
    KLANG = 600
    KLINKLANG = 601
    TYNAMO = 602
    EELEKTRIK = 603
    EELEKTROSS = 604
    ELGYEM = 605
    BEHEEYEM = 606
    LITWICK = 607
    LAMPENT = 608
    CHANDELURE = 609
    AXEW = 610
    FRAXURE = 611
    HAXORUS = 612
    CUBCHOO = 613
    BEARTIC = 614
    CRYOGONAL = 615
    SHELMET = 616
    ACCELGOR = 617
    STUNFISK = 618
    MIENFOO = 619
    MIENSHAO = 620
    DRUDDIGON = 621
    GOLETT = 622
    GOLURK = 623
    PAWNIARD = 624
    BISHARP = 625
    BOUFFALANT = 626
    RUFFLET = 627
    BRAVIARY = 628
    VULLABY = 629
    MANDIBUZZ = 630
    HEATMOR = 631
    DURANT = 632
    DEINO = 633
    ZWEILOUS = 634
    HYDREIGON = 635
    LARVESTA = 636
    VOLCARONA = 637
    COBALION = 638
    TERRAKION = 639
    VIRIZION = 640
    TORNADUS = 641
    THUNDURUS = 642
    RESHIRAM = 643
    ZEKROM = 644
    LANDORUS = 645
    KYUREM = 646
    KELDEO = 647
    MELOETTA = 648
    GENESECT = 649
    CHESPIN = 650
    QUILLADIN = 651
    CHESNAUGHT = 652
    FENNEKIN = 653
    BRAIXEN = 654
    DELPHOX = 655
    FROAKIE = 656
    FROGADIER = 657
    GRENINJA = 658
    BUNNELBY = 659
    DIGGERSBY = 660
    FLETCHLING = 661
    FLETCHINDER = 662
    TALONFLAME = 663
    SCATTERBUG = 664
    SPEWPA = 665
    VIVILLON = 666
    LITLEO = 667
    PYROAR = 668
    FLABEBE = 669
    FLOETTE = 670
    FLORGES = 671
    SKIDDO = 672
    GOGOAT = 673
    PANCHAM = 674
    PANGORO = 675
    FURFROU = 676
    ESPURR = 677
    MEOWSTIC = 678
    HONEDGE = 679
    DOUBLADE = 680
    AEGISLASH = 681
    SPRITZEE = 682
    AROMATISSE = 683
    SWIRLIX = 684
    SLURPUFF = 685
    INKAY = 686
    MALAMAR = 687
    BINACLE = 688
    BARBARACLE = 689
    SKRELP = 690
    DRAGALGE = 691
    CLAUNCHER = 692
    CLAWITZER = 693
    HELIOPTILE = 694
    HELIOLISK = 695
    TYRUNT = 696
    TYRANTRUM = 697
    AMAURA = 698
    AURORUS = 699
    SYLVEON = 700
    HAWLUCHA = 701
    DEDENNE = 702
    CARBINK = 703
    GOOMY = 704
    SLIGGOO = 705
    GOODRA = 706
    KLEFKI = 707
    PHANTUMP = 708
    TREVENANT = 709
    PUMPKABOO = 710
    GOURGEIST = 711
    BERGMITE = 712
    AVALUGG = 713
    NOIBAT = 714
    NOIVERN = 715
    XERNEAS = 716
    YVELTAL = 717
    ZYGARDE = 718
    DIANCIE = 719
    HOOPA = 720
    VOLCANION = 721
    ROWLET = 722
    DARTRIX = 723
    DECIDUEYE = 724
    LITTEN = 725
    TORRACAT = 726
    INCINEROAR = 727
    POPPLIO = 728
    BRIONNE = 729
    PRIMARINA = 730
    PIKIPEK = 731
    TRUMBEAK = 732
    TOUCANNON = 733
    YUNGOOS = 734
    GUMSHOOS = 735
    GRUBBIN = 736
    CHARJABUG = 737
    VIKAVOLT = 738
    CRABRAWLER = 739
    CRABOMINABLE = 740
    ORICORIO = 741
    CUTIEFLY = 742
    RIBOMBEE = 743
    ROCKRUFF = 744
    LYCANROC = 745
    WISHIWASHI = 746
    MAREANIE = 747
    TOXAPEX = 748
    MUDBRAY = 749
    MUDSDALE = 750
    DEWPIDER = 751
    ARAQUANID = 752
    FOMANTIS = 753
    LURANTIS = 754
    MORELULL = 755
    SHIINOTIC = 756
    SALANDIT = 757
    SALAZZLE = 758
    STUFFUL = 759
    BEWEAR = 760
    BOUNSWEET = 761
    STEENEE = 762
    TSAREENA = 763
    COMFEY = 764
    ORANGURU = 765
    PASSIMIAN = 766
    WIMPOD = 767
    GOLISOPOD = 768
    SANDYGAST = 769
    PALOSSAND = 770
    PYUKUMUKU = 771
    TYPE_NULL = 772
    SILVALLY = 773
    MINIOR = 774
    KOMALA = 775
    TURTONATOR = 776
    TOGEDEMARU = 777
    MIMIKYU = 778
    BRUXISH = 779
    DRAMPA = 780
    DHELMISE = 781
    JANGMOO = 782
    HAKAMOO = 783
    KOMMOO = 784
    TAPU_KOKO = 785
    TAPU_LELE = 786
    TAPU_BULU = 787
    TAPU_FINI = 788
    COSMOG = 789
    COSMOEM = 790
    SOLGALEO = 791
    LUNALA = 792
    NIHILEGO = 793
    BUZZWOLE = 794
    PHEROMOSA = 795
    XURKITREE = 796
    CELESTEELA = 797
    KARTANA = 798
    GUZZLORD = 799
    NECROZMA = 800
    MAGEARNA = 801
    MARSHADOW = 802
    POIPOLE = 803
    NAGANADEL = 804
    STAKATAKA = 805
    BLACEPHALON = 806
    ZERAORA = 807
    MELTAN = 808
    MELMETAL = 809
    GROOKEY = 810
    THWACKEY = 811
    RILLABOOM = 812
    SCORBUNNY = 813
    RABOOT = 814
    CINDERACE = 815
    SOBBLE = 816
    DRIZZILE = 817
    INTELEON = 818
    SKWOVET = 819
    GREEDENT = 820
    ROOKIDEE = 821
    CORVISQUIRE = 822
    CORVIKNIGHT = 823
    BLIPBUG = 824
    DOTTLER = 825
    ORBEETLE = 826
    NICKIT = 827
    THIEVUL = 828
    GOSSIFLEUR = 829
    ELDEGOSS = 830
    WOOLOO = 831
    DUBWOOL = 832
    CHEWTLE = 833
    DREDNAW = 834
    YAMPER = 835
    BOLTUND = 836
    ROLYCOLY = 837
    CARKOL = 838
    COALOSSAL = 839
    APPLIN = 840
    FLAPPLE = 841
    APPLETUN = 842
    SILICOBRA = 843
    SANDACONDA = 844
    CRAMORANT = 845
    ARROKUDA = 846
    BARRASKEWDA = 847
    TOXEL = 848
    TOXTRICITY = 849
    SIZZLIPEDE = 850
    CENTISKORCH = 851
    CLOBBOPUS = 852
    GRAPPLOCT = 853
    SINISTEA = 854
    POLTEAGEIST = 855
    HATENNA = 856
    HATTREM = 857
    HATTERENE = 858
    IMPIDIMP = 859
    MORGREM = 860
    GRIMMSNARL = 861
    OBSTAGOON = 862
    PERRSERKER = 863
    CURSOLA = 864
    SIRFETCHD = 865
    MR_RIME = 866
    RUNERIGUS = 867
    MILCERY = 868
    ALCREMIE = 869
    FALINKS = 870
    PINCURCHIN = 871
    SNOM = 872
    FROSMOTH = 873
    STONJOURNER = 874
    EISCUE = 875
    INDEEDEE = 876
    MORPEKO = 877
    CUFANT = 878
    COPPERAJAH = 879
    DRACOZOLT = 880
    ARCTOZOLT = 881
    DRACOVISH = 882
    ARCTOVISH = 883
    DURALUDON = 884
    DREEPY = 885
    DRAKLOAK = 886
    DRAGAPULT = 887
    ZACIAN = 888
    ZAMAZENTA = 889
    ETERNATUS = 890
    KUBFU = 891
    URSHIFU = 892
    ZARUDE = 893
    REGIELEKI = 894
    REGIDRAGO = 895
    GLASTRIER = 896
    SPECTRIER = 897
    CALYREX = 898
    WYRDEER = 899
    KLEAVOR = 900
    URSALUNA = 901
    BASCULEGION = 902
    SNEASLER = 903
    OVERQWIL = 904
    ENAMORUS = 905
    SPRIGATITO = 906
    FLORAGATO = 907
    MEOWSCARADA = 908
    FUECOCO = 909
    CROCALOR = 910
    SKELEDIRGE = 911
    QUAXLY = 912
    QUAXWELL = 913
    QUAQUAVAL = 914
    LECHONK = 915
    OINKOLOGNE = 916
    DUDUNSPARCE = 917
    TAROUNTULA = 918
    SPIDOPS = 919
    NYMBLE = 920
    LOKIX = 921
    RELLOR = 922
    RABSCA = 923
    GREAVARD = 924
    HOUNDSTONE = 925
    FLITTLE = 926
    ESPATHRA = 927
    FARIGIRAF = 928
    WIGLETT = 929
    WUGTRIO = 930
    DONDOZO = 931
    VELUZA = 932
    FINIZEN = 933
    PALAFIN = 934
    SMOLIV = 935
    DOLLIV = 936
    ARBOLIVA = 937
    CAPSAKID = 938
    SCOVILLAIN = 939
    TADBULB = 940
    BELLIBOLT = 941
    VAROOM = 942
    REVAVROOM = 943
    ORTHWORM = 944
    TANDEMAUS = 945
    MAUSHOLD = 946
    CETODDLE = 947
    CETITAN = 948
    FRIGIBAX = 949
    ARCTIBAX = 950
    BAXCALIBUR = 951
    TATSUGIRI = 952
    CYCLIZAR = 953
    PAWMI = 954
    PAWMO = 955
    PAWMOT = 956
    WATTREL = 957
    KILOWATTREL = 958
    BOMBIRDIER = 959
    SQUAWKABILLY = 960
    FLAMIGO = 961
    KLAWF = 962
    NACLI = 963
    NACLSTACK = 964
    GARGANACL = 965
    GLIMMET = 966
    GLIMMORA = 967
    SHROODLE = 968
    GRAFAIAI = 969
    FIDOUGH = 970
    DACHSBUN = 971
    MASCHIFF = 972
    MABOSSTIFF = 973
    BRAMBLIN = 974
    BRAMBLEGHAST = 975
    GIMMIGHOUL = 976
    GHOLDENGO = 977
    GREAT_TUSK = 978
    BRUTE_BONNET = 979
    _980 = 980
    SANDY_SHOCKS = 981
    SCREAM_TAIL = 982
    FLUTTER_MANE = 983
    SLITHER_WING = 984
    ROARING_MOON = 985
    IRON_TREADS = 986
    _987 = 987
    IRON_MOTH = 988
    IRON_HANDS = 989
    IRON_JUGULIS = 990
    IRON_THORNS = 991
    IRON_BUNDLE = 992
    IRON_VALIANT = 993
    TING_LU = 994
    CHIEN_PAO = 995
    WO_CHIEN = 996
    CHI_YU = 997
    KORAIDON = 998
    MIRAIDON = 999
    TINKATINK = 1000
    TINKATUFF = 1001
    TINKATON = 1002
    CHARCADET = 1003
    ARMAROUGE = 1004
    CERULEDGE = 1005
    TOEDSCOOL = 1006
    TOEDSCRUEL = 1007
    KINGAMBIT = 1008
    CLODSIRE = 1009
    ANNIHILAPE = 1010

    def __str__(self) -> str:
        return self.name.replace("_", " ").title()
