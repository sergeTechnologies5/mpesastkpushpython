# PYTHON STK PUSH DOCUMENTATION
## I found it hard to read the mpesa(api) documenation and implement it so I decided to give devs a clear code that they can just use in any python framework.

## I will later convert the code to either flask or django so that it will have a practical impact for devs who would like to use it in their projects. I mean it has very little impact for raw python .

## The code is well tested and works perfectly as for this time's requirements . This code is free ,most of it is referenced from other dev's repos who tried to make mpesa intergration simpler. I added a callback code that handles receiving acknowledgements from mpesa for any transaction you make with their api I mean any http request to their api

##  The pygetapikey is a simple test to get an API KEY from mpesa. I will be abit mechanical so  I wont explain how the MPESA API works , I will just give working code for devs who understand how it works but they cant put up the code easily. 

### NB : No external library or api is used I used raw request to write the code