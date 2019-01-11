#include <GL/glut.h>
#include "Graphics.h"
#include <math.h>

double PI = 3.1415926;
double ANGLE_STEP = 0.0314125936;

void setColor(double red, double green, double blue) {
     glColor3d(red, green, blue);
}

void quitKey(unsigned char key, int x, int y) {
     if (key == 'q') exit(0);
}

void GraphicsSetup(int argc, char **argv) {
     glutInit(&argc, argv);
     glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
	 glutInitWindowPosition(WINDOW_X,WINDOW_Y);
	 glutInitWindowSize(WINDOW_HEIGHT,WINDOW_WIDTH);
	 glutCreateWindow("COSC1315 - Graphics Lab");
	 glClearColor(WHITE,0.0);
	 glOrtho(0,WINDOW_WIDTH, 0,WINDOW_HEIGHT,0,1);
     glutKeyboardFunc(quitKey);
  }

void clearWindow() {
     glClear(GL_COLOR_BUFFER_BIT);
}

void drawTriangle(int x1, int y1, int x2, int y2, int x3, int y3) {
     glBegin(GL_LINE_STRIP);
     glVertex2i(x1,y1);
     glVertex2i(x2,y2);
     glVertex2i(x3,y3);
     glVertex2i(x1,y1);
     glEnd();
     glFlush();
}

void drawFilledTriangle(int x1, int y1, int x2, int y2, int x3, int y3) {
     glBegin(GL_POLYGON);
     glVertex2i(x1,y1);
     glVertex2i(x2,y2);
     glVertex2i(x3,y3);
     glVertex2i(x1,y1);
     glEnd();
     glFlush();
}

void drawLine(int x1, int y1, int x2, int y2) {
     glBegin(GL_LINE_STRIP);
     glVertex2i(x1,y1);
     glVertex2i(x2,y2);
     glEnd();
     glFlush();
}

void drawBox(int x1, int y1, int x2, int y2) {
     glBegin(GL_LINE_STRIP);
     glVertex2i(x1,y1);
     glVertex2i(x2,y1);
     glVertex2i(x2,y2);
     glVertex2i(x1,y2);
     glVertex2i(x1,y1);
     glEnd();
     glFlush();
}

void drawFilledBox(int x1, int y1, int x2, int y2) {
     glBegin(GL_POLYGON);
     glVertex2i(x1,y1);
     glVertex2i(x2,y1);
     glVertex2i(x2,y2);
     glVertex2i(x1,y2);
     glVertex2i(x1,y1);
     glEnd();
     glFlush();
}

void drawCircle(int x1, int y1, int radius) {
     double angle;
     int X, Y;
     double dradius;
     dradius = (double)radius;

     glBegin(GL_LINE_STRIP);
     for (angle=0;angle< 2.0*PI + ANGLE_STEP; angle += ANGLE_STEP) {
         X = x1 + (int)(dradius * cos(angle));
         Y = y1 + (int)(dradius * sin(angle));
         glVertex2i(X,Y);
     }
     glEnd();
     glFlush();
}         

void drawFilledCircle(int x1, int y1, int radius) {
     double angle;
     double dradius;
     int X0, Y0, X1, Y1;

     dradius = (double)radius;
     glBegin(GL_TRIANGLES);
     X1 = x1 + radius;
     Y1 = y1;
     for (angle=0;angle< 2.0*PI + ANGLE_STEP; angle += ANGLE_STEP) {
         X0 = X1;
         Y0 = Y1;
         X1 = x1 + (int)(dradius * cos(angle));
         Y1 = y1 + (int)(dradius * sin(angle));
         glVertex2i(x1,y1);
         glVertex2i(X0,Y0);
         glVertex2i(X1,Y1);
     }
     glEnd();
     glFlush();
}         


