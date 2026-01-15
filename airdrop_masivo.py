~ $ import time

from web3 import Web3



# --- 1. TU CONFIGURACIÓN ---

RPC_URL = "https://polygon-rpc.com"

CONTRATO_TOKEN = "0xc9b356b1dBf3750F5EC401c9cE2C2746d79391eE"

LLAVE_PRIVADA = "6a0272fdcc69a324ecbc4cb66f2069e4441e0d16923b35b2078c8e071631c776"

MI_DIRECCION = "0xc371aaaebbfcea3ab7e985287fadae6f436f15a2"

CANTIDAD_A_ENVIAR = 500  # Cuántos tokens $57 para cada uno



# --- 2. LISTA DE LAS 150 WALLETS EXTRAÍDAS ---

wallets = [

    "0x29e7df7b6a1b2b07b731457f499e1696c60e2c4e", "0x111cff45948819988857bbf1966a0399e0d1141e", 

    "0x9ee91f9f426fa633d227f7a9b000e28b9dfd8599", "0x4aaabfe1cfed908760c123cab5c885297df5a28b",

    "0x0c2d08f81d111876872fe350e0a560b9d11bb399", "0x5ee84d30c7ee57f63f71c92247ff31f95e26916b",

    "0xee235a7dfeac038f6551b1fc4d022d69f1381f33", "0x3d66dd9c9cf2ee749f1fa743dad336b84254221f",

    "0x65c14d348aca2c7cde813e8f1ac5c8df1081dd3b", "0xcd531ae9efcce479654c4926dec5f6209531ca7b",

    "0x5450c96314a70802370ed7909bab7985d84c3bcb", "0x000a25e9148ba7f910100864fd07fa225cb57c11",

    "0x0bb1810061c2f5b2088054ee184e6c79e1591101", "0xa7fa0d1b251eb2c362e6cd017fdec09a973385fe",

    "0xd426037bcf28fc4ea3730525ff8b3d2de412257d", "0xd1401338d673aad5bdb2ce0652104a09f5ab9bc4",

    "0xd520e3662f2af962dd6b42ad5b26d6ffca561296", "0x8727740093a1998cdda74fdce6631a7b33450595",

    "0x4c75da685109945d235c42151f9ec21162ee07be", "0xe3ecd65cf2ad2eba2aa2be1d0894753b2172abd1",

    "0x2a3dd3eb832af982ec71669e178424b10dca2ede", "0x3d3323f905077d799a33f62d4800ba7cf11b4408",

    "0xed5c546e063fdff031a6ebe5f9009666d800af5f", "0xf7f741e29828da8500a5daae6a348008fe3a5816",

    "0x87bc1b3e3db2a4c8d8def57817addc93afd5ea3f", "0x0305c18771cd11b36dcfa610bcc8837f814746f1",

    "0xf90f431375d55a2673addbef69fd86c277f7ff64", "0x51c72848c68a965f66fa7a88855f9f7784502a7f",

    "0xdfd207984ef43a3f639d1d1b12205fac6137d0ce", "0x22b1cbb8d98a01a3b71d034bb899775a76eb1cc2",

    "0x8cc57372203f05056dffb4ed110d82b164760940", "0x819f3450da6f110ba6ea52195b3beafa246062de",

    "0x0a6518544405f17885e97896b3de7db3e186cc17", "0xabee4dd3be138d33ae79be154f20238fbe008fd2",

    "0x28c6c06298d514db089934071355e5743bf21d60", "0xbd02c51150a4ab6ce97b9de2025644594f3e75b8",

    "0x5a5ba9d00323dc77f6a73db6a5d2282b4b98effb", "0xdf638df23915d45f04bf4e59dd368d7b3bbfa58e",

    "0x935d2e470284fb536227a76a723f96a94efae6a9", "0xe45e12b44fca87e42dbc63a67bf5aa8ab800f459",

    "0xe74b28c2eae8679e3ccc3a94d5d0de83ccb84705", "0x290a6a7460b308ee3f19023d2d00de604bcf5b42",

    "0xa8d7142ed2a5d4f871bd7d22612afd87cf23fb58", "0x2aea39e27fc87de4a63963687c6e188f062197b4",

    "0xff71a37cd33c8d40ed32c33412be539403581d78", "0x046d158f5ba7d4a8aa0b2f4fa39c987b7e21f822",

    "0xd7efcbb86efdd9e8de014dafa5944aae36e817e4", "0x700eacb2cab3e288904881ef1d9f9f81cb35a5f1",

    "0x267d9810d3c1548b50f2ab71df8c5d4f1bcaebb1", "0x748de14197922c4ae258c7939c7739f3ff1db573",

    "0x9e5de432ac02b054835920232b4fa6a04c2bf6fd", "0xcffad3200574698b78f32232aa9d63eabd290703",

    "0xf8191d98ae98d2f7abdfb63a9b0b812b93c873aa", "0xc29681ab980f5779381194ec75f27c6d742e2120",

    "0x8843ca4adfc80e331164c3531585436cce739af1", "0x6a526f6b9e5bf45a7df235f73a2da47424aac7a3",

    "0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43", "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0",

    "0xc669b5f25f03be2ac0323037cb57f49eb543657a", "0x52256ef863a713ef349ae6e97a7e8f35785145de",

    "0x095e64b9333e4f46b606fca1dfab676cf266e7cd", "0x7c8242866297b70f0e26927027d3781f6e5fca97",

    "0x1f5ba50353dea5e954d9c6fe2a7c58cd622f5da8", "0x6697e711b7f7440720d1c4fac253262f0a1ce8da",

    "0xadec0cdc6adabe44f461b48358d4a8d3a7d62a95", "0x87d93d9b2c672bf9c9642d853a8682546a5012b5",

    "0xa9fd6d6f28e25c8d13dcb5d1ac6bfd9889e86f3d", "0xc3bd6653be08b9393c2f3ee704b0173e36f3e67d",

    "0x07834b06b5756056e065c0bd1639761ab8297513", "0xf60c2ea62edbfe808163751dd0d8693dcb30019c",

    "0xace78296d7ed0d11634b69c4b5ed3fb54eb0966e", "0xf636688e15411594e57e8cd770d36136a4ca23b1",

    "0x476f67aff04968111bfc0e2318b52d5d4d7f1ee5", "0xb280935547d2f3e3a86815464040689c8e7b49128",

    "0x9f530366659695dcb1975c684daa5de720cb5356", "0xa51cdaccb66c808f78da33c38197bc80935b9cdd",

    "0x84447e76dbc84bda71ed480095913f5a22a3d93c", "0x4f151a723c3a86a9d60dfe061632c2c0d81b9774",

    "0x80036918fecb63469d2762867ce1c6bc244c6159", "0xe33d40a79a18605c89431f21832a194f8cd3ee58",

    "0x7830c87c02e56aff27fa8ab1241711331fa86f43", "0x96ba4d04d889426b4b1eb051bf5daf00ec331004",

    "0x0fb52e637c407b82bd443bf30df8a4

The program import is not installed. Install it by executing:

 pkg install imagemagick

The program from is not installed. Install it by executing:

 pkg install mailutils

RPC_URL: command not found

CONTRATO_TOKEN: command not found

LLAVE_PRIVADA: command not found

MI_DIRECCION: command not found

CANTIDAD_A_ENVIAR: command not found

No command wallets found, did you mean:

 Command kwalletd6 in package kf6-kwallet from the x11-repo repository

 Command allec in package texlive-bin

0x29e7df7b6a1b2b07b731457f499e1696c60e2c4e,: command not found

0x9ee91f9f426fa633d227f7a9b000e28b9dfd8599,: command not found

0x0c2d08f81d111876872fe350e0a560b9d11bb399,: command not found

0xee235a7dfeac038f6551b1fc4d022d69f1381f33,: command not found

0x65c14d348aca2c7cde813e8f1ac5c8df1081dd3b,: command not found

0x5450c96314a70802370ed7909bab7985d84c3bcb,: command not found

0x0bb1810061c2f5b2088054ee184e6c79e1591101,: command not found

0xd426037bcf28fc4ea3730525ff8b3d2de412257d,: command not found

0xd520e3662f2af962dd6b42ad5b26d6ffca561296,: command not found

0x4c75da685109945d235c42151f9ec21162ee07be,: command not found

0x2a3dd3eb832af982ec71669e178424b10dca2ede,: command not found

0xed5c546e063fdff031a6ebe5f9009666d800af5f,: command not found

0x87bc1b3e3db2a4c8d8def57817addc93afd5ea3f,: command not found

0xf90f431375d55a2673addbef69fd86c277f7ff64,: command not found

0xdfd207984ef43a3f639d1d1b12205fac6137d0ce,: command not found

0x8cc57372203f05056dffb4ed110d82b164760940,: command not found

0x0a6518544405f17885e97896b3de7db3e186cc17,: command not found

0x28c6c06298d514db089934071355e5743bf21d60,: command not found

0x5a5ba9d00323dc77f6a73db6a5d2282b4b98effb,: command not found

0x935d2e470284fb536227a76a723f96a94efae6a9,: command not found

0xe74b28c2eae8679e3ccc3a94d5d0de83ccb84705,: command not found

0xa8d7142ed2a5d4f871bd7d22612afd87cf23fb58,: command not found

0xff71a37cd33c8d40ed32c33412be539403581d78,: command not found

0xd7efcbb86efdd9e8de014dafa5944aae36e817e4,: command not found

0x267d9810d3c1548b50f2ab71df8c5d4f1bcaebb1,: command not found

0x9e5de432ac02b054835920232b4fa6a04c2bf6fd,: command not found

0xf8191d98ae98d2f7abdfb63a9b0b812b93c873aa,: command not found

0x8843ca4adfc80e331164c3531585436cce739af1,: command not found

0xa9d1e08c7793af67e9d92fe308d5697fb81d3e43,: command not found

0xc669b5f25f03be2ac0323037cb57f49eb543657a,: command not found

0x095e64b9333e4f46b606fca1dfab676cf266e7cd,: command not found

0x1f5ba50353dea5e954d9c6fe2a7c58cd622f5da8,: command not found

0xadec0cdc6adabe44f461b48358d4a8d3a7d62a95,: command not found

0xa9fd6d6f28e25c8d13dcb5d1ac6bfd9889e86f3d,: command not found

0x07834b06b5756056e065c0bd1639761ab8297513,: command not found

0xace78296d7ed0d11634b69c4b5ed3fb54eb0966e,: command not found

0x476f67aff04968111bfc0e2318b52d5d4d7f1ee5,: command not found

0x9f530366659695dcb1975c684daa5de720cb5356,: command not found

0x84447e76dbc84bda71ed480095913f5a22a3d93c,: command not found

0x80036918fecb63469d2762867ce1c6bc244c6159,: command not found

0x7830c87c02e56aff27fa8ab1241711331fa86f43,: command not found

>
