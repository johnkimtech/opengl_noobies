
#version 330

in vec3 v_color;
in float t;
out vec3 f_color;

float speed = 10.0;
void main() {
    float r = sin(v_color.x + t*speed);
    float g = cos(v_color.y + t*speed);
    float b = cos(v_color.z + t / 2*speed);

    f_color = (vec3(r,g,b)+2)/3;
}