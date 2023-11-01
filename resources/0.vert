#version 330

in vec2 in_xt;
in vec3 in_color;
out vec3 v_color;
out float t;
float speed = 10.;
void main() {
    v_color = in_color;
    float x = in_xt.x;
    t = in_xt.y;
    float y = sin(x * 10 + t * speed);
    gl_Position = vec4(x, y, 0.0, 1.0);
}