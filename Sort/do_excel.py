import xlrd, xlwt


class DoExcel():
    def __init__(self, file_path, sheets):
        self.file_path = file_path
        self.sheets = sheets


    def write_excel(self):
        # res, fields = excute_sql()
        # 将结果写进excel
        workbook = xlwt.Workbook()
        # 新建sheet
        for sheet in self.sheets:
            workbook.add_sheet(sheet, cell_overwrite_ok=True)
        sh = workbook.get_sheet()
        # s = workbook.add_sheet(self.sheets[1], cell_overwrite_ok=True)

        # 将表的字段写入excel
        # for field in range(len(fields)):
        #     workbook.get_sheet()
        #     sheet.write(0, field, fields[field][0])
        # # 结果写入excel
        # for row in range(1, len(res)+1):
        #     for col in range(len(fields)):
        #         sheet.write(row, col, res[row-1][col])
        # excel保存为文件
        workbook.save(self.file_path)


if __name__ == '__main__':
    file_path = r'F:\py_project\Sort\select_M.xls'
    sheets = ['xx001', 'xx003']
    a = DoExcel(file_path, sheets)
    a.write_excel()

    print('ok01')
