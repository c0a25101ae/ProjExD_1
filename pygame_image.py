import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") # 練習1
    bg_img_flip = pg.transform.flip(bg_img, True, False) # 課題8：背景画像を反転
    kk_img_3 = pg.image.load("fig/3.png") # 練習3：こうかとんの画像の読み込み
    kk_img_3 = pg.transform.flip(kk_img_3, True, False) # 練習3：こうかとん反転
    kk_rect = kk_img_3.get_rect() # 練習10-1：こうかとんRectを取得する
    kk_rect.center = 300, 200 # 練習10-2：こうかとんの初期座標の設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() # 練習10-3：すべてのキーの状態の取得
        move = 1
        not_moov = 0
        move_x = -move
        move_y = not_moov
        if key_lst[pg.K_UP]: # 練習10-4：上矢印キーが押されたら
            move_y = -move # 縦に-1動かす
            kk_rect.move_ip((move_x, move_y))
        if key_lst[pg.K_DOWN]: # 練習10-4：下矢印キーが押されたら
            move_y = move # 縦に+1動かす
            kk_rect.move_ip((move_x, move_y))
        if key_lst[pg.K_RIGHT]: # 練習10-4：右矢印キーが押されたら
            move_x = move # 横に+1動かす
            kk_rect.move_ip((move_x, move_y))
        if key_lst[pg.K_LEFT]: # 練習10-4：左矢印キーが押されたら
            move_x = -move - 1 # 横に-1動かす
            kk_rect.move_ip((move_x, move_y))

        x = tmr % 3200 # 課題5：背景画像移動用の変数
        screen.blit(bg_img, [-x, 0]) # 練習2
        screen.blit(bg_img_flip, [-x + 1600, 0]) # 練習7：背景画像Surfaceをもう1回ブリっと
        screen.blit(bg_img, [-x + 3200, 0]) # 練習9：右側にoriginal2をblit
        screen.blit(kk_img_3, kk_rect) # 練習4：こうかとんSurfaceの描画
        pg.display.update()
        tmr += 1        
        clock.tick(200) # 課題6：FPSの変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()