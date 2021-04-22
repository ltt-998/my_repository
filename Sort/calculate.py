import xlrd

class Calculate():
    def __init__(self,e_file,sheet):
        self.e_file = e_file
        self.sheet = sheet


    def get_excel_data(self):
        all_goods_num = []
        for n in range(1, self.sheet.nrows):
            num = self.sheet.cell_value(n, 1)
            all_goods_num.append(num)
        print(all_goods_num)

        min_num = min(all_goods_num)
        max_num = max(all_goods_num)


        all_goods_sale = []
        for s in range(1, self.sheet.nrows):
            sale = self.sheet.cell_value(s, 2)
            all_goods_sale.append(sale)
        print(all_goods_sale)

        min_sale = min(all_goods_sale)
        max_sale = max(all_goods_sale)

# 公式 ：Y=[ X -min(X) ] / [ max(X) - min (X) ]，结果保留4位小数
# Y：周期内该商品变量得分
# X：周期内该商品变量之和，min(x)为商品所在商品表下该变量最小的值，max(x)为商品所在商品表下该变量最大的值

        Y_all_goods_num = []
        for agn in all_goods_num:
            Y_agn = (agn - min_num)/(max_num - min_num)
            Y_all_goods_num.append(Y_agn)
        # print(Y_all_goods_num)


        Y_all_goods_sale = []
        for ags in all_goods_sale:
            Y_ags = (ags - min_sale)/(max_sale - min_sale)
            Y_all_goods_sale.append(Y_ags)
        # print(Y_all_goods_sale)

        # 用户反馈分(N) =[ Y(收藏量) + Y(访客数) + Y(访问量) ] / 3
        # [收藏量]：周期内同一人重复收藏，计算1次；[访客数]：PV；[访问量]：UV

        Y_visitors = []
        for v in range(1,self.sheet.nrows):
            Y_v = self.sheet.cell_value(v,4)
            Y_visitors.append(Y_v)
        print(Y_visitors)

        Y_visit_num = []
        for v in range(1,self.sheet.nrows):
            Y_v_n = self.sheet.cell_value(v,5)
            Y_visit_num.append(Y_v_n)
        print(Y_visit_num)


        # 商品质量分(M) = [ ( Y(销量)+Y(销售额) ] / 2     [销量]：下单即算；[销售额]：下单

        for m in range(0, len(all_goods_num)):
            quality_M = (Y_all_goods_num[m] + Y_all_goods_sale[m]) / 2
            feedback_N = (Y_visitors[m] + Y_visit_num[m]) / 3
            final_calculate = 0.1*quality_M + 0.2*feedback_N +0.08+0.1
            # print(quality_M)
            # print(feedback_N)
            print(final_calculate)



if __name__ == '__main__':
    # e_file = xlrd.open_workbook('select_M.xls')
    # sheet = e_file.sheet_by_name('M_homestay')
    # print(1)
    # a = Calculate(e_file,sheet).get_excel_data()
    pass





