
		
		printf("set size square\n");
		printf("set xrange [0:%d]\n");
		printf("set yrange [0:%d]\n");
		printf("plot \"-\" w p pt 7 ps 2\n");
		for(i=0;i<N;i++) {
			printf("%f %f \n", rx[i],ry[i]);
		}
		printf("e\n");
	
	tempo = tempo + dt;
	}
	return 0;
}
