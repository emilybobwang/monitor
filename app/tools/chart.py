# -*-coding: utf-8 -*-
from pyecharts import Liquid
import  datetime

class Chart(object):
    def liqiud_html(self,chart_id,title,val):
        liquid = Liquid(
            "{}-{}".format(
                self.datetime, title
            ),
            title_pos="center",
            width="100%",
            title_color="white",
            title_text_size=14,
            height=300
        )

        liquid.chart_id = chart_id
        liquid.add("", [round(val / 100, 4)])
        return liquid.render_embed()

    @property
    def datetime(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")