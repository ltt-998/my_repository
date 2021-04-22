import configparser

class GetConf():
    def __init__(self, conf_path):
        self.conf_path = conf_path
        self.cf = configparser.ConfigParser()
        self.cf.read(self.conf_path, encoding='utf-8')

    def get_conf(self, option, ection):
        return self.cf.get(option, ection)

    def get_cycle_1(self):
        num_cycle = self.cf.get('CYCLE_1', 'num_cycle')
        sale_cycle = self.cf.get('CYCLE_1', 'sale_cycle')
        collect_cycle = self.cf.get('CYCLE_1', 'collect_cycle')
        visitor_cycle = self.cf.get('CYCLE_1', 'visitor_cycle')
        visit_num_cycle = self.cf.get('CYCLE_1', 'visit_num_cycle')
        return num_cycle, sale_cycle, collect_cycle, visitor_cycle, visit_num_cycle

    def get_cycle_2(self):
        pass



if __name__ == '__main__':
    a = GetConf(r'F:\py_project\Sort\sort_conf')
    num_cycle, sale_cycle, collect_cycle, visitor_cycle, visit_num_cycle = a.get_cycle_1()
    print(num_cycle, sale_cycle, collect_cycle, visitor_cycle, visit_num_cycle)

