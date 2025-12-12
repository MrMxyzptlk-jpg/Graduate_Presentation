load '/home/prof/EXCITING/exciting_neon/tools/tutorial_scripts/gnuplot_settings.gp'

incident(x) = 1
unset ytics
unset xtics
set ylabel "Intensidad" offset 0, 0
set xlabel "Energía" offset 0, 0
unset key
unset obj 1

set arrow from graph 0.0, graph 0.0 to graph 0.0, graph 1.0 head lc "black" lw borderWidth
set arrow from graph 0.0, graph 0.0 to graph 1.0, graph 0.0 head lc "black" lw borderWidth

set sample 100

set yrange [0:1.5]
set xrange [0:1]

plot incident(x) w lp lc rgb "black"

set table "incident.dat"
plot incident(x)
unset table