#include <math.h>
#include <GL/glut.h>
#include "Graphics.h"
 
#define RADIUS      25
#define NUMBALLS    2

void check_collision(int i, int j);

int xPos[NUMBALLS], yPos[NUMBALLS], i, j;
float speed = 0.1;
float deltaX[NUMBALLS], deltaY[NUMBALLS];

void initPosition() {
    for(int i = 0; i < NUMBALLS; i++) {
        xPos[i] = (i+1) * (RADIUS + 30);
        yPos[i] = (i+2) * (RADIUS);
        deltaX[i] = 3.0 * speed;
        deltaY[i] = 2.0 * speed;
    }
}

void animate() { 
    for(int i = 0; i < NUMBALLS; i++ ) {
        xPos[i] += deltaX[i];
        yPos[i] += deltaY[i];
        // check for wall collisions
        if((xPos[i] >= WINDOW_WIDTH-RADIUS) || (xPos[i] <= RADIUS))
            deltaX[i] = -deltaX[i];
        if((yPos[i] >= WINDOW_HEIGHT-RADIUS) || (yPos[i] <= RADIUS))
            deltaY[i] = -deltaY[i];
    }
    for(int i = 0; i < NUMBALLS -1; i++)
        for(int j = i + 1; j < NUMBALLS; j++ )
            check_collision(i,j);
    glutPostRedisplay();
}

void check_collision(int i, int j) {
    // see if ball i collided with ball j
    double dist, x1, x2, y1, y2, dx, dy;
    double vx1, vx2, vy1, vy2;
    x1 = xPos[i]; x2 = xPos[j]; dx = x2 - x1;
    y1 = yPos[i]; y2 = yPos[j]; dy = y2 - y1;
    dist = sqrt((dx*dx) + (dy*dy));
    if (dist > 2.0 * RADIUS) return;   // no collision

    double ax, ay, vn1,vn2,vt1, vt2, v1np,v2np, v1tp, v2tp;

    ax = dx/dist; ay = dy/dist;
    vx1 = deltaX[i]; vx2 = deltaX[j];  // X velocities
    vy1 = deltaY[i]; vy2 = deltaY[j];  // Y velocities
    
    vn1 = (vx1 * ax + vy1 * ay); vt1 = (-vx1 * ay + vy1 * ax);
    vn2 = (vx2 * ax + vy2 * ay); vt2 = (-vx2 * ay + vy2 * ax);

    v1np = vn1 + (vn2 - vn1); v2np = vn2 + (vn1 - vn2);

    vx1 = v1np * ax - vt1 * ay; vy1 = v2np * ay + vt1 * ax;
    vx2 = v2np * ax - vt2 * ay; vy2 = v2np * ay + vt2 * ax;

    deltaX[i] = vx1; deltaY[i]= vy1;
    deltaX[j] = vx2; deltaY[j]= vy2;

    while(dist > 2.0 * RADIUS) {
        // check for wall collisions
        if((xPos[i] >= WINDOW_WIDTH-RADIUS) || (xPos[i] <= RADIUS))
            deltaX[i] = -deltaX[i];
        if((yPos[i] >= WINDOW_HEIGHT-RADIUS) || (yPos[i] <= RADIUS))
            deltaY[i] = -deltaY[i];
        // check for wall collisions
        //if((xPos[j] >= WINDOW_WIDTH-RADIUS) || (xPos[j] <= RADIUS))
        //    deltaX[j] = -deltaX[j];
        //if((yPos[i] >= WINDOW_HEIGHT-RADIUS) || (yPos[i] <= RADIUS))
        //    deltaY[j] = -deltaY[j];
    }
}
void drawScene(void) { 
    clearWindow();
    setColor(RED) ;
    drawFilledCircle(xPos[0],yPos[0],RADIUS) ;
    setColor(BLUE) ;
    drawFilledCircle(xPos[1],yPos[1],RADIUS) ;
    setColor(GREEN) ;
    drawFilledCircle(xPos[2],yPos[2],RADIUS) ;
    setColor(YELLOW) ;
    drawFilledCircle(xPos[3],yPos[3],RADIUS) ;
    setColor(BLACK) ;
    drawFilledCircle(xPos[4],yPos[4],RADIUS) ;

    /*(for( i = 0; i < NUMBALLS; i++ ) {
        setColor(RED);
        drawFilledCircle(xPos[i],yPos[i],RADIUS);
    }
    */

    glEnd();
    glFlush();
    glutSwapBuffers();
}

int main(int argc, char * argv[]) {
    GraphicsSetup(argc, argv);
    initPosition();
    glutDisplayFunc(drawScene);
    glutIdleFunc(animate);
    glutMainLoop();
}
