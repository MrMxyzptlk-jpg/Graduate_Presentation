load '/home/prof/EXCITING/exciting_neon/tools/tutorial_scripts/gnuplot_settings.gp'

incident(x) = 1
i = (0,1)
lorentzian(x,a,b) = (b / pi) / ((x-a)**2 - b**2 + 1e-5*i) 
transmited(x) = incident(x) - lorentzian(x,0.33333,9e-6) - lorentzian(x,0.533333,3e-5) - lorentzian(x,0.73333,1.7e-5)

unset ytics
unset xtics
set ylabel "Intensidad" offset 0, 0 
set xlabel "Energía" offset 0, 0
unset key
unset obj 1

set arrow from graph 0.0, graph 0.0 to graph 0.0, graph 1.0 head lc "black" lw borderWidth
set arrow from graph 0.0, graph 0.0 to graph 1.0, graph 0.0 head lc "black" lw borderWidth

set sample 200

set yrange [0:1.5]
set xrange [0:1]

plot transmited(x) w lp lc rgb "black"


set table "transmited.dat"
plot transmited(x)
unset table