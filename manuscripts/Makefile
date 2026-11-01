PAPERS = einstein_gaps curvature_extremals einstein_realization almost_kahler_einstein
OUT ?= ../.build/manuscripts

.PHONY: all clean
all:
	mkdir -p $(OUT)
	@set -e; for paper in $(PAPERS); do \
	  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(OUT) $$paper.tex; \
	  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$(OUT) $$paper.tex; \
	  cp $(OUT)/$$paper.pdf $$paper.pdf; \
	done

clean:
	rm -f $(OUT)/*.aux $(OUT)/*.log $(OUT)/*.out $(OUT)/*.toc
