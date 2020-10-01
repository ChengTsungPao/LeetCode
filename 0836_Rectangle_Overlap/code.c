bool isRectangleOverlap(int* rec1, int rec1Size, int* rec2, int rec2Size){
    for(int i=0;i<2;i++){
        if( ( (((rec1[0+i]<rec2[0+i] && rec1[0+i]>rec2[2+i]) || (rec1[0+i]>rec2[0+i] && rec1[0+i]<rec2[2+i])) || 
              ((rec1[2+i]<rec2[0+i] && rec1[2+i]>rec2[2+i]) || (rec1[2+i]>rec2[0+i] && rec1[2+i]<rec2[2+i])))
              ||
              (((rec2[0+i]<rec1[0+i] && rec2[0+i]>rec1[2+i]) || (rec2[0+i]>rec1[0+i] && rec2[0+i]<rec1[2+i])) || 
              ((rec2[2+i]<rec1[0+i] && rec2[2+i]>rec1[2+i]) || (rec2[2+i]>rec1[0+i] && rec2[2+i]<rec1[2+i]))) )==0 ){
            return 0;
        }        
    }
    return 1;
}