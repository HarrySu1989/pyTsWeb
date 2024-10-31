function flask_url(q1,offset,v) {
   // alert(q1)
    const myArray = q1.split(",");
    s0 = ""
    for( i=0;i<myArray.length;i++)
    {
        if(i===offset)
        {
            s0+=v;
        }
        else
        {
            s0+=myArray[i];
        }
        if(i!==myArray.length-1)
        {
            s0+=",";
        }
    }
    // alert(q1+"\n"+s0)
    var url = window.location.href;
    var buf = url.split('?');
    location.assign(buf[0] + "?q=" + s0 );
}
