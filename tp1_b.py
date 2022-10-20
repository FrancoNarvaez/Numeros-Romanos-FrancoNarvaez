
import unittest

def conversor(romano):
    letra_1 = 0
    letra_2 = 0
    letra_3 = 0    
    letra_4 = 0
    letra_5 = 0

    for x in romano:
        if (x) == "I":
            letra_1 = 1 + letra_1
        elif (x) == "V":
            letra_2 = 5
        elif (x) == "X":
            letra_3 = 10 + letra_3
        elif (x) == "L":
            letra_4 = 50
        elif (x) == "C":
            letra_5 = 100
    
    valor = [letra_1,letra_2, letra_3, letra_4, letra_5]

    for i in valor:
        a = 0
        b = 0
        if  valor[i] >= valor[i + 1]:
            b = valor[i + 1] - valor[i]
        if valor[i] < valor[i + 1]:
            b = valor[i + 1] + valor[i]
        c = a + b
        return c

class TestRomanToNumber(unittest.TestCase):
    def test_1(self):
        self.assertEqual(conversor("I") ,1)
    def test_2(self):
        self.assertEqual(conversor("II"),2)
    def test_3(self):
        self.assertEqual(conversor("III"),3)
    def test_4(self):
        self.assertEqual(conversor("IV"),4)
    def test_5(self):
        self.assertEqual(conversor("V"),5)
    def test_6(self):
        self.assertEqual(conversor("VI"),6)
    def test_7(self):
        self.assertEqual(conversor("VII"),7)
    def test_8(self):
        self.assertEqual(conversor("VIII"),8)
    def test_9(self):
        self.assertEqual(conversor("IX"),9)
    def test_10(self):
        self.assertEqual(conversor("X"),10)
    def test_11(self):
        self.assertEqual(conversor("XI"),11)
    def test_12(self):
        self.assertEqual(conversor("XII"),12)
    def test_13(self):
        self.assertEqual(conversor("XIII"),13)
    def test_14(self):
        self.assertEqual(conversor("XIV"),14)
    def test_15(self):
        self.assertEqual(conversor("XV"),15)
    def test_16(self):
        self.assertEqual(conversor("XVI"),16)
    def test_17(self):
        self.assertEqual(conversor("XVII"),17)
    def test_18(self):
        self.assertEqual(conversor("XVIII"),18)
    def test_19(self):
        self.assertEqual(conversor("XIX"),19)
    def test_20(self):
        self.assertEqual(conversor("XX"),20)
    def test_21(self):
        self.assertEqual(conversor("XXI"),21)
    def test_22(self):
        self.assertEqual(conversor("XXII"),22)
    def test_23(self):
        self.assertEqual(conversor("XXIII"),23)
    def test_24(self):
        self.assertEqual(conversor("XXIV"),24)
    def test_25(self):
        self.assertEqual(conversor("XXV"),25)
    def test_26(self):
        self.assertEqual(conversor("XXVI"),26)
    def test_27(self):
        self.assertEqual(conversor("XXVII"),27)
    def test_28(self):
        self.assertEqual(conversor("XXVIII"),28)
    def test_29(self):
        self.assertEqual(conversor("XXIX"),29)
    def test_30(self):
        self.assertEqual(conversor("XXX"),30)
    def test_31(self):
        self.assertEqual(conversor("XXXI"),31)
    def test_32(self):
        self.assertEqual(conversor("XXXII"),32)
    def test_33(self):
        self.assertEqual(conversor("XXXIII"),33)
    def test_34(self):
        self.assertEqual(conversor("XXXIV"),34)
    def test_35(self):
        self.assertEqual(conversor("XXXV"),35)
    def test_36(self):
        self.assertEqual(conversor("XXXVI"),36)
    def test_37(self):
        self.assertEqual(conversor("XXXVII"),37)
    def test_38(self):
        self.assertEqual(conversor("XXXVIII"),38)
    def test_39(self):
        self.assertEqual(conversor("XXXIX"),39)
    def test_40(self):
        self.assertEqual(conversor("XL"),40)
    def test_41(self):
        self.assertEqual(conversor("XLI"),41)
    def test_42(self):
        self.assertEqual(conversor("XLII"),42)
    def test_43(self):
        self.assertEqual(conversor("XLIII"),43)
    def test_44(self):
        self.assertEqual(conversor("XLIV"),44)
    def test_45(self):
        self.assertEqual(conversor("XLV"),45)
    def test_46(self):
        self.assertEqual(conversor("XLVI"),46)
    def test_47(self):
        self.assertEqual(conversor("XLVII"),47)
    def test_48(self):
        self.assertEqual(conversor("XLVIII"),48)
    def test_49(self):
        self.assertEqual(conversor("XLIX"),49)
    def test_50(self):
        self.assertEqual(conversor("L"),50)
    def test_51(self):
        self.assertEqual(conversor("LI"),51)
    def test_52(self):
        self.assertEqual(conversor("LII"),52)
    def test_53(self):
        self.assertEqual(conversor("LIII"),53)
    def test_54(self):
        self.assertEqual(conversor("LIV"),54)
    def test_55(self):
        self.assertEqual(conversor("LV"),55)
    def test_56(self):
        self.assertEqual(conversor("LVI"),56)
    def test_57(self):
        self.assertEqual(conversor("LVII"),57)
    def test_58(self):
        self.assertEqual(conversor("LVIII"),58)
    def test_59(self):
        self.assertEqual(conversor("LIX"),59)
    def test_60(self):
        self.assertEqual(conversor("LX"),60)
    def test_61(self):
        self.assertEqual(conversor("LXI"),61)
    def test_62(self):
        self.assertEqual(conversor("LXII"),62)
    def test_63(self):
        self.assertEqual(conversor("LXIII"),63)
    def test_64(self):
        self.assertEqual(conversor("LXIV"),64)
    def test_65(self):
        self.assertEqual(conversor("LXV"),65)
    def test_66(self):
        self.assertEqual(conversor("LXVI"),66)
    def test_67(self):
        self.assertEqual(conversor("LXVII"),67)
    def test_68(self):
        self.assertEqual(conversor("LXVIII"),68)
    def test_69(self):
        self.assertEqual(conversor("LXIX"),69)
    def test_70(self):
        self.assertEqual(conversor("LXX"),70)
    def test_71(self):
        self.assertEqual(conversor("LXXI"),71)
    def test_72(self):
        self.assertEqual(conversor("LXXII"),72)
    def test_13(self):
        self.assertEqual(conversor("XIII"),73)
    def test_74(self):
        self.assertEqual(conversor("LXXIV"),74)
    def test_75(self):
        self.assertEqual(conversor("LXXV"),75)
    def test_76(self):
        self.assertEqual(conversor("LXXVI"),76)
    def test_77(self):
        self.assertEqual(conversor("LXXVII"),77)
    def test_78(self):
        self.assertEqual(conversor("LXXVIII"),78)
    def test_79(self):
        self.assertEqual(conversor("LXXIX"),79)
    def test_80(self):
        self.assertEqual(conversor("LXXX"),80)
    def test_81(self):
        self.assertEqual(conversor("LXXXI"),81)
    def test_82(self):
        self.assertEqual(conversor("LXXXII"),82)
    def test_83(self):
        self.assertEqual(conversor("LXXXIII"),83)
    def test_84(self):
        self.assertEqual(conversor("LXXXIV"),84)
    def test_85(self):
        self.assertEqual(conversor("LXXXV"),85)
    def test_86(self):
        self.assertEqual(conversor("LXXXVI"),86)
    def test_87(self):
        self.assertEqual(conversor("LXXXVII"),87)
    def test_88(self):
        self.assertEqual(conversor("LXXXVIII"),88)
    def test_89(self):
        self.assertEqual(conversor("LXXXIX"),89)
    def test_90(self):
        self.assertEqual(conversor("XC"),90)
    def test_91(self):
        self.assertEqual(conversor("XCI"),91)
    def test_92(self):
        self.assertEqual(conversor("XCII"),92)
    def test_93(self):
        self.assertEqual(conversor("XCIII"),93)
    def test_94(self):
        self.assertEqual(conversor("XCIV"),94)
    def test_95(self):
        self.assertEqual(conversor("XCV"),95)
    def test_96(self):
        self.assertEqual(conversor("XCVI"),96)
    def test_97(self):
        self.assertEqual(conversor("XCVII"),97)
    def test_98(self):
        self.assertEqual(conversor("XCVIII"),98)
    def test_99(self):
        self.assertEqual(conversor("XCIX"),99)
    def test_100(self):
        self.assertEqual(conversor("C"),100)

if __name__=='__main__':
    unittest.main()