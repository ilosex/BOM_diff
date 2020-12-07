import pathlib

from Src import SheetOperation


class DiffChecker:
    def __init__(self):
        self.old_BOM = ''
        self.new_BOM = ''
        self.diff = ''
        self.deleted = []
        self.appended = []
        self.modified = []

    def set_old_BOM(self, path):
        self.old_BOM = path

    def set_new_BOM(self, path):
        self.new_BOM = path

    def set_diff(self, path):
        self.diff = path

    def list_construct(self, *args):
        result = [[f'Старый BOM: {pathlib.Path(self.old_BOM).name}'],
                  [f'Новый BOM: {pathlib.Path(self.new_BOM).name}'],
                  [],
                  [],
                  ['Component', 'Quantity', 'Commentary'],
                  []
                  ]
        inserts = [['Deleted:', '', ''],
                   ['Appended:', '', ''],
                   ['Modified:', '', '']
                   ]
        for n in range(3):
            result.append(inserts[n])
            for row in args[n]:
                result.append(row.to_list())
            result.append(['', '', ''])
        return result

    def diff_finder(self):
        old_sheet = SheetOperation.Sheet(self.old_BOM).worksheet_parser()
        new_sheet = SheetOperation.Sheet(self.new_BOM).worksheet_parser()
        save = SheetOperation.SheetFormer(self.diff)
        translate = save.element_translation
        old_element = old_sheet.pop()
        new_element = new_sheet.pop()
        while len(old_sheet) > 0 and len(new_sheet) > 0:
            if new_element == old_element:
                old_element = old_sheet.pop()
                new_element = new_sheet.pop()
            else:
                if old_element.name != new_element.name:
                    if old_element.name > new_element.name:
                        self.deleted.append(translate(old_element, 'Deleted'))
                        old_element = old_sheet.pop()
                    else:
                        self.appended.append(translate(new_element, 'Appended'))
                        new_element = new_sheet.pop()
                else:
                    self.modified.append(translate(new_element, f'Изменено количество, было: {old_element.quantity}'))
                    old_element = old_sheet.pop()
                    new_element = new_sheet.pop()
        else:
            if len(self.deleted) == len(self.appended) == len(self.modified) == 0:
                return list('Файлы BOM одинаковы!')
            else:
                self.deleted.sort()
                self.appended.sort()
                self.modified.sort()
                save.save_sheet(self.list_construct(self.deleted, self.appended, self.modified))
