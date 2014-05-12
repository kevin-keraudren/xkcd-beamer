name=presentation

all:
	pdflatex --shell-escape ${name}

clean:
	if [ -e ${name}.out ]; then rm *.aux *.log *.nav *.out *.snm *.toc; fi
	if [ -e auto/ ]; then rm -r auto; fi
