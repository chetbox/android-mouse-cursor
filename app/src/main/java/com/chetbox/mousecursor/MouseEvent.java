package com.chetbox.mousecursor;

/**
 * Created by chetan on 30/04/15.
 */
public class MouseEvent {

    public static final int
            MOVE_UP = 0,
            MOVE_DOWN = 1,
            MOVE_LEFT = 2,
            MOVE_RIGHT = 3,
            LEFT_CLICK = 4;

    public final int direction;

    public MouseEvent(int direction) {
        this.direction = direction;
    }
}
