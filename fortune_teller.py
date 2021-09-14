from random import Random


class FortuneTeller:
    def tell(self) -> str:
        oracles = [
            f"今日のラッキー牌は{self.lucky_tile()}です。 "
            + f"*{self.lucky_yaku()}* が和了れそうな一日。",
            self.message()
        ]

        return '\n'.join(oracles)

    def lucky_yaku(self) -> str:
        random = Random().random()
        yaku = self.__pick_yaku_group(random)
        i = int(random * len(yaku))
        return yaku[i]

    def lucky_tile(self) -> str:
        random = Random().random()

        NUMBER_OF_KINDS = 34
        x = int(random * NUMBER_OF_KINDS) + 1

        if 1 <= x <= 9:
            return f":mj_m{x}:"
        elif 10 <= x <= 18:
            return f":mj_s{x - 9}:"
        elif 19 <= x <= 27:
            return f":mj_p{x - 18}:"
        else:
            # XXX: 字牌だけ読みが末尾にあるので別個にリストを作った
            #      リストを1-originにしたのでそのまま呼べる
            return self.EMOJI_ZI_PAI[x - 27]

    def message(self) -> str:
        random = Random().random()

        i = int(random * len(self.MESSAGES))
        return self.MESSAGES[i]

    def __pick_yaku_group(self) -> list:
        x = Random().random() * 100

        if x < 0.001:
            return self.TOO_LARELY_YAKUMAN
        elif x < 0.1:
            return self.YAKUMAN
        elif x < 20:
            return self.YAKU_BASED_ON_LUCK
        else:
            return self.SIX_HAN_HANDS + self.THREE_HAN_HANDS + \
                self.THREE_HAN_HANDS + self.ONE_HAN_HANDS

    # XXX: 0-originにしたいから0番目を空にしておく
    EMOJI_ZI_PAI = ['',
                    ':mj_z1_ton:',
                    ':mj_z2_nan:',
                    ':mj_z3_sha:',
                    ':mj_z4_pei:',
                    ':mj_z5_haku:',
                    ':mj_z6_hatsu:',
                    ':mj_z7_chun:']
    ONE_HAN_HANDS = ['断么九',
                     '平和',
                     '一盃口']
    TWO_HAN_HANDS = ['三色同順',
                     '対々和',
                     '七対子',
                     '一通',
                     '混全帯么九',
                     '三暗刻',
                     '三色同刻',
                     '三槓子',
                     '混老頭',
                     '小三元']
    THREE_HAN_HANDS = ['混一色',
                       '純全帯么九',
                       '二盃口']
    SIX_HAN_HANDS = ['清一色']
    YAKUMAN = ['四暗刻',
               '大三元',
               '国士無双',
               '四喜和',
               '字一色',
               '清老頭',
               '地和',
               '緑一色',
               '九連宝燈',
               '四槓子',
               '八連荘']
    YAKU_BASED_ON_LUCK = ['門前清自摸和',
                          '一発',
                          '海底撈月',
                          '河底撈魚',
                          '嶺上開花',
                          '搶槓',
                          'ダブルリーチ']
    TOO_LARELY_YAKUMAN = ['天和',
                          '地和',
                          '純正九蓮宝燈']
    MESSAGES = [
        '他家からのリーチが怖く見える日。自分の手なりと相談して。',
        'ピンチをチャンスに変えられる星回り。いつもは九種九牌を倒すあなたも国士無双を目指してみて。',
        '筋を切ったら引掛けにあたり、テンパイ気配の現物么九牌を切ったら他家の国士にあたるような日。今日は守りの練習日にして。',
        '最悪な配牌からでもリーチにたどり着ける運気を感じます。9順目まで諦めないで。',
        'ドラを大事にしたい日。孤立牌と思っても12順目あたりには思わぬ発見があるかも。',
        '追い風を受けてあなたは一層輝きます。自風の対子は大事に。',
        '今日のあなたには向かい風が吹きます。風牌の重なりより数牌のつながりを感じて。',
        '純粋な雀力が試される日。いつも以上に牌効率を意識して。',
        '麻雀の基本はメン・タン・ピン。門前での手作りがあなたを成長させます。',
        'ダマテンに要注意。4順目のあの手出しはテンパイ気配かも。',
        '手を進めたいという強い思いが上家から有効牌を引き出します。配牌で三色の鼓動を感じて。',
        'あなたの心はスリルを求めている。役満チャンスを活かせるかも。まずは三暗刻を意識。',
        'とにかく手が進まない一日。一向聴で粘らず、河を見て降りることを忘れないで。',
        '一見染めてほしいように見える手でも、こだわりすぎるとダマテンに当たるかも。',
        '大明槓に要注意。相手のドラを増やしたり、引いてきた嶺上牌は他家の当たり牌かも。',
        'チャンスは至るところにある。相手の加槓を見逃さず槍槓を決めて。',
        '星はあなたの頭上に輝く。三面張につなげてオープンリーチで勝負。',
        '運気は下降気味。他家からの運気をもらうためにも、有効な鳴きを意識してみて。',
        '積み上げてきたものが崩れ落ちる日。東発で跳満を上がっても油断は禁物。',
        '縦に重なる日。最悪でも対々和、うまくいけば四暗刻。でもポンの連呼は要注意。',
        '老頭牌に好かれる日。混老頭や純全帯を絡めて満貫を狙ってみて。',
        'テンパイ料が大事になる日。最後まで諦めずにいたら海底摸月や河底撈魚にも出会える。',
        '無意味な1翻に翻弄される日。8翻あれば十分倍満は狙えるからドラは捨てても大丈夫。'
    ]
