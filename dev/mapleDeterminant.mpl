read("matrix_INPUT.dat"):
detM := LinearAlgebra[Determinant](matrix_INPUT):
fd := fopen("detM.dat", WRITE):
fprintf(fd,"%s",convert(detM,string)):
fclose(fd):