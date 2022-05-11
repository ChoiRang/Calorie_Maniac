from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import Line, Pie
from random import randrange


class GraphBase:
    def pie_base(self, name=['탄수화물', '단백질', '지방', '당류'], value=[123, 456, 789, 321], title='음식 영양 정보') -> Pie:
        a = value
        v = [[i] for i in a]
        k = name
        p = (
            Pie(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS)
                ).add("", [list(z) for z in zip(k, v)], rosetype="radius", radius=["30%", "60%"]
                      ).set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='top', formatter="{d} %")
                                        ).set_global_opts(title_opts=opts.TitleOpts(title=title),
                                                          tooltip_opts=opts.TooltipOpts(formatter="{b}: {c} kcal"),
                                                          legend_opts=opts.LegendOpts(type_='scroll', pos_bottom="60%",
                                                                                      pos_right="0%",
                                                                                      orient="vertical",
                                                                                      legend_icon='pin'))
        )
        return p

    def line_month_base(self, day, exercise_kcal, food_kcal) -> Line:
        total_job_rate = Line(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS
                                                      , animation_opts=opts.AnimationOpts(animation_delay=1000
                                                                                          ,
                                                                                          animation_easing="elasticOut")))
        total_job_rate.add_xaxis(day).add_yaxis('운동한 칼로리', exercise_kcal)

        ## 추가 꺾은선
        l = (Line(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS,
                                          animation_opts=opts.AnimationOpts(animation_delay=1000,
                                                                            animation_easing="elasticOut")
                                          ))).set_global_opts(
            title_opts=opts.TitleOpts(
                title="월간 리포트"),
            yaxis_opts=opts.AxisOpts(name="kcal", type_="value"),
            xaxis_opts=opts.AxisOpts(name='날짜', type_="value"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="slider")],
            legend_opts=opts.LegendOpts(pos_left="40%", legend_icon='pin'),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
        ).set_series_opts(label_opts=opts.LabelOpts(is_show=True)).add_xaxis(day
                                                                             ).add_yaxis('먹은 음식 칼로리', food_kcal)

        ## 합치기
        l = l.overlap(total_job_rate)

        return l
