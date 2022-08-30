#version 150
uniform float time;
uniform vec2 resolution;
uniform vec2 mouse;
uniform vec3 spectrum;
uniform sampler2D texture0;
uniform sampler2D texture1;
uniform sampler2D texture2;
uniform sampler2D texture3;
uniform sampler2D prevFrame;
uniform sampler2D prevPass;
#define MAX_RAY_BOUNCES         3.0
#define BAUBLE_REFLECTIVITY     0.70
in VertexData
{
    vec4 v_position;
    vec3 v_normal;
    vec2 v_texcoord;
} inData;
out vec4 fragColor;
vec3 lightPos=(vec3(-10.0,100.0,600.0));
vec3 lightDirection=normalize(vec3(18,15+6*sin(time),-4.0));
float hash11(float p){
return fract(sin(p)*478.4345);}
float plane(vec3 p){return  p.y+1.3; }
float terrain(vec3 p){
 float displacement = sin(-5.40 * p.x) * sin(1 * p.y*0.1) *10* sin(5.0 * p.z) * 0.25;
return  p.y+sin(p.x/3)+cos(p.z/6)*3+displacement/3;
}
float sphere(vec3 ro,vec3 p,float s)
{
return length(ro-p)-s;
}
float opu(float a , float b ){
return min(a,b);
}
vec2 map(vec3 ro){
float res=0.0;
float color=0;
res=opu(sphere(ro,vec3(0.0,1.52 ,3.0),0.5),plane(ro));
res=opu(res,terrain(ro));
res=opu(res,sphere(ro,vec3(1.0,.252 ,3.29),1.5));
res=opu(res,sphere(ro,vec3(2.0,1.252 ,2.5),0.5));
if(res==sphere(ro,vec3(0.0,1.52 ,3.0),0.5))color=2.;
if(res==terrain(ro))color=3.;
if(res==plane(ro))color=4.;
if(res==sphere(ro,vec3(1.0,.252 ,3.29),1.5))color=5.;
if(res==sphere(ro,vec3(2.0,1.252 ,2.5),0.5))color=2.;
return vec2(res,color);}
vec3 computNorm(vec3 p){
vec2 eps=vec2(0.001,0.0);
return normalize(vec3(
map(p+eps.xyy).x-map(p-eps.xyy).x,
map(p+eps.yxy).x-map(p-eps.yxy).x,
map(p+eps.yyx).x-map(p-eps.yyx).x));}
float hash12(float p){
return fract(sin(p)*478.4345);}
float diffuse(vec3 normal)
{
return max( 0.0, dot(normal,lightDirection    ));
}
float specular(vec3 normal,vec3 dir)
{
vec3 h= normalize(normal-dir+lightDirection);
return  pow(max(dot(h,normal),0.0 ),400.0);
}
float shadow( in vec3 ro, in vec3 rd, float mint, float maxt )
{
    for( float t=mint; t < maxt; )
    {
        float h = map(ro + rd*t).x;
        if( h<0.001 )
            return 0.0;
        t += h;
    }
    return 1.0;
}
vec4 march(vec3 ro,vec3 rd)
{
float d=0.0;float material=0;
  vec3 nor = computNorm( ro );
for(int i=0;i<600;i++)
{
d=map(ro).x;
material=map(ro).y;
ro+=rd*d;
if(d<0.01)
{ float ligthDistance= length(normalize(lightPos)-normalize(ro));
//vec3 color= vec3(diffuse( computNorm( ro ))*ligthDistance);
//vec3 color= vec3(1)*(diffuse(computNorm( ro )*-abs(ligthDistance)));
vec3 color=vec3(0);
if(material==2)color+=vec3(ro.y*.51,0,-3.0+-ligthDistance);
if(material==3)color+=vec3(-1.0,0.8*-ligthDistance,ro.z*-0.040);
if(material==4){color+=vec3(-1,-1,-0.09*ro.z);;ro+=reflect(ro,normalize(computNorm(ro )))*0.952;}
if(material==5){color+=vec3(ro.y*0.52,-.50,-0.9*ro.z);ro+=reflect(ro,normalize(computNorm(ro )))*0.1952;}
//color+= vec3(1)*ligthDistance;
//color*=-0.5+1;
 //color +=ligthDistance*specularity(computNorm(-ro),lightPos)*vec3(.00,1.90,0.70);/
 color += 0.1*specular( computNorm(ro ),rd)*vec3(010.01);
 color +=diffuse( computNorm(ro ))*vec3(0.81);
 float dom = smoothstep(0, 1, reflect(lightDirection, computNorm(ro )).x )*0.5;
  color+=vec3(dom);
color*=shadow(ro,lightDirection,2,5);
return vec4 (color,0.0);
}
}
return vec4(0.0);
}
vec4 render(vec3 ro,vec3 rd){
return march(ro,rd);
}
void main(void)
{
    vec2 uv = -1. + 2. * inData.v_texcoord;
    uv.x*=1.5;
    vec3 ro=vec3(0.0,  -0.0023,-2.20);
    vec3 rd=normalize(vec3((uv),1.0));
    vec4  res=render(ro,rd);
    fragColor = vec4(res.rgb,1.0);
}
