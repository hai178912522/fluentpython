# -*- coding: utf-8 -*-
# @Time : 2022/7/15 20:44
# @Author : ZZZZZHHHHH
# @FileName: 理想类.py
# @Software: PyCharm


class SideBar:
    DIV: str = 'div'
    H1: str = 'h1'
    MORE: str = 'more'
    MORE_ITEMS_LENGTH: int = 3
    SHOULD_COMPRESS_HTML: bool = True

    def __init__(
            self,
            title: str,
            menu_items: [str],
            more: str = MORE,
            more_itmes_length: int = MORE_ITEMS_LENGTH,
        should_compress_html: bool = SHOULD_COMPRESS_HTML
    ) -> None:
        self.title = title
        self.more = more
        self.more_itmes_length = more_itmes_length
        self.should_compress_html = should_compress_html
        self.menu_items = menu_items

    def __len__(self):
        return len(self.menu_items)

    def __repr__(self):
        return f'SideBar:{len(self)} menu items'

    @classmethod
    def _header(cls, title):
        return cls._build_header(cls.H1, title)

    @classmethod
    def _body(cls, menu_items: [str], should_compress_html: bool) -> str:
        split_char = cls._get_split_char(should_compress_html)
        return split_char.join(
            list(cls._build_body(cls.DIV, menu_items))
        )
    @classmethod
    def _more(cls,more):
        return cls._build_more(cls.DIV, more)

    @staticmethod
    def _build_header(tag_name: str, title: str) -> str:
        return f'<{tag_name}>{title}</{tag_name}>'

    @staticmethod
    def _build_body(tag_name: str, menu_items: [str]) -> str:
        for meun_item in menu_items:
            yield f'<{tag_name}>{meun_item}</{tag_name}>'

    @staticmethod
    def _build_more(tag_name: str, text: str) -> str:
        return f'<{tag_name}>{text}</{tag_name}>'
    @staticmethod
    def _get_split_char(should_compress_html: bool) -> str:
        return '' if should_compress_html else '\n'
    def _is_few_items(self):
        return len(self) < self.more_itmes_length

    def build(self) -> str:
        header = self._header(self.title)
        body = self._body(self.menu_items, self.should_compress_html)
        footer = self._more(self.more) if self._is_few_items() else ''
        split_char = self._get_split_char(self.should_compress_html)
        return split_char.join([header, body, footer])

if __name__ == '__main__':
    side_bar = SideBar('DEMO SIDE BAR',
                       ['item 1', 'item 2', 'item 3'],
                       should_compress_html=False,
                       more_itmes_length=4
                       )
    print(side_bar.build())