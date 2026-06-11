import os
import math
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont

# Path configuration
src_image_path = "/Users/chris/.gemini/antigravity-ide/brain/fd5cb153-2e7d-4cdb-bd73-5c59fa8176b6/media__1781101202286.png"
dst_video_path = "/Users/chris/Documents/Capstone/purityloop_trailer.mp4"
dst_brain_path = "/Users/chris/.gemini/antigravity-ide/brain/fd5cb153-2e7d-4cdb-bd73-5c59fa8176b6/purityloop_trailer.mp4"

width, height = 1280, 720
fps = 30
duration_sec = 30
total_frames = fps * duration_sec  # 900 frames

# Load fonts
font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
font_bold_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
font_title = ImageFont.truetype(font_bold_path, 48)
font_subtitle = ImageFont.truetype(font_path, 28)
font_hud = ImageFont.truetype(font_bold_path, 20)
font_micro = ImageFont.truetype(font_path, 11)

# Define crop coordinates from source image (1024 x 633)
crops_coords = {
    "chris": (330, 140, 670, 400),
    "naomi": (25, 350, 185, 595),
    "talvin": (205, 350, 365, 595),
    "kong": (415, 350, 570, 595),
    "feng": (610, 350, 770, 595),
    "georgene": (800, 350, 960, 595)
}

# Load main delegation image
img_src = Image.open(src_image_path).convert("RGBA")

# Extract profiles and save in memory
profiles = {}
for name, coords in crops_coords.items():
    profiles[name] = img_src.crop(coords)

# Create Widescreen Cinematic Video Frames
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(dst_video_path, fourcc, float(fps), (width, height))

def draw_text_centered(draw, text, y, font, color=(255, 255, 255, 255)):
    tw = draw.textlength(text, font=font)
    draw.text(((width - tw) // 2, y), text, font=font, fill=color)

def draw_typewriter_text(draw, text, y, font, progress, color=(255, 255, 255, 255)):
    char_count = int(len(text) * progress)
    visible_text = text[:char_count]
    tw = draw.textlength(text, font=font)
    draw.text(((width - tw) // 2, y), visible_text, font=font, fill=color)

def apply_glitch(img, magnitude=8):
    arr = np.array(img)
    h_img, w_img, c = arr.shape
    num_slices = 12
    slice_h = h_img // num_slices
    for s in range(num_slices):
        offset = np.random.randint(-magnitude, magnitude)
        if offset == 0:
            continue
        y1 = s * slice_h
        y2 = (s + 1) * slice_h
        arr[y1:y2, :, :] = np.roll(arr[y1:y2, :, :], offset, axis=1)
    return Image.fromarray(arr)

def draw_reticle(draw, x1, y1, x2, y2, color=(16, 185, 129, 255), L=20, w=3):
    # Top-Left
    draw.line([(x1, y1), (x1 + L, y1)], fill=color, width=w)
    draw.line([(x1, y1), (x1, y1 + L)], fill=color, width=w)
    # Top-Right
    draw.line([(x2, y1), (x2 - L, y1)], fill=color, width=w)
    draw.line([(x2, y1), (x2, y1 + L)], fill=color, width=w)
    # Bottom-Left
    draw.line([(x1, y2), (x1 + L, y2)], fill=color, width=w)
    draw.line([(x1, y2), (x1, y2 - L)], fill=color, width=w)
    # Bottom-Right
    draw.line([(x2, y2), (x2 - L, y2)], fill=color, width=w)
    draw.line([(x2, y2), (x2, y2 - L)], fill=color, width=w)

# Timeline definition (900 frames total - 30 seconds):
# 0 to 180: Scene 1: "6 MEMBERS" - Show overall group members. (6s)
# 180 to 270: Scene 2: Backend Squad (Naomi & Talvin). (3s)
# 270 to 360: Scene 3: Integration Squad (Kong). (3s)
# 360 to 450: Scene 4: Frontend Squad (Feng & Georgene). (3s)
# 450 to 540: Scene 5: "1 TEAM" - Cut to Chris (Project Manager). (3s)
# 540 to 630: Scene 6: "14-WEEK DELIVERY". (3s)
# 630 to 720: Scene 7: "WORKING TOWARDS ONE GOAL...". (3s)
# 720 to 900: Scene 8: Climax - "PURITYLOOP AI" tagline questions. (6s)

for f in range(total_frames):
    frame_img = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(frame_img)
    
    # Cinematic slate background gradient
    for y in range(height):
        factor = y / float(height)
        r = int(10 + (2 - 10) * factor)
        g = int(14 + (4 - 14) * factor)
        b = int(22 + (8 - 22) * factor)
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))
        
    bar_h = 90
    
    # Check flash transitions
    flash_frames = [180, 270, 360, 450, 540, 720]
    flash_alpha = 0
    for ff in flash_frames:
        if ff <= f < ff + 15:
            flash_alpha = int(255 * (1.0 - (f - ff) / 15.0))
            
    # Apply scene logic
    if 0 <= f < 180:
        # Scene 1: 6 MEMBERS
        progress = f / 180.0
        fade_out = min(1.0, (180 - f) / 15.0)
        
        # Whole team delegation diagram zooming in slowly (slightly offset downwards to make room for title)
        scale = 0.70 + progress * 0.08
        dw, dh = img_src.size
        sw, sh = int(dw * scale), int(dh * scale)
        img_resized = img_src.resize((sw, sh), Image.Resampling.LANCZOS)
        px = (width - sw) // 2
        # Position image lower down (170 instead of 105 center) to prevent overlapping with text
        py = 180 + int(progress * 10)
        frame_img.paste(img_resized, (px, py), img_resized)
        
        hud_box_y = height - bar_h - 45
        draw.rectangle([30, hud_box_y, width - 30, hud_box_y + 35], fill=(15, 23, 42, 180), outline=(52, 211, 153, 100), width=1)
        draw.text((45, hud_box_y + 10), "HUD: INFERENCE STREAM ACTIVE // SCANNING GROUP MEMBERS...", font=font_micro, fill=(52, 211, 153, 200))
        
        # Position title "6 MEMBERS" higher up (at y=100 instead of 110)
        tw_progress = min(1.0, f / 90.0)
        draw_typewriter_text(draw, "6 MEMBERS", 98, font_title, tw_progress, (255, 255, 255, int(255 * fade_out)))
        
    elif 180 <= f < 270:
        # Scene 2: Backend Squad (Naomi & Talvin) (90 frames / 3 seconds)
        sf = f - 180
        progress = sf / 90.0
        card1 = profiles["naomi"]
        card2 = profiles["talvin"]
        cw, ch = card1.size
        
        scale = 1.0 + progress * 0.22
        sw, sh = int(cw * scale), int(ch * scale)
        card1_r = card1.resize((sw, sh), Image.Resampling.LANCZOS)
        card2_r = card2.resize((sw, sh), Image.Resampling.LANCZOS)
        
        gap = 60
        total_w = sw * 2 + gap
        start_x = (width - total_w) // 2
        py = (height - sh) // 2 - 20 - int(progress * 15)
        
        frame_img.paste(card1_r, (start_x, py), card1_r)
        frame_img.paste(card2_r, (start_x + sw + gap, py), card2_r)
        
        draw_reticle(draw, start_x, py, start_x + sw, py + sh, color=(16, 185, 129, 200))
        draw_reticle(draw, start_x + sw + gap, py, start_x + sw + gap + sw, py + sh, color=(16, 185, 129, 200))
        
        if sf < 5:
            frame_img = apply_glitch(frame_img, magnitude=12)
            draw = ImageDraw.Draw(frame_img)
            
        draw_text_centered(draw, "SQUAD 01: BACKEND SQUAD", 120, font_hud, (52, 211, 153, 255))
        draw_text_centered(draw, "ONG JIA XIN (NAOMI)  |  TALVIN LEE GEN WEI", 580, font_subtitle, (255, 255, 255, 255))
        
    elif 270 <= f < 360:
        # Scene 3: Integration Squad (Kong) (90 frames / 3 seconds)
        sf = f - 270
        progress = sf / 90.0
        card = profiles["kong"]
        cw, ch = card.size
        
        scale = 1.05 + progress * 0.18
        sw, sh = int(cw * scale), int(ch * scale)
        card_resized = card.resize((sw, sh), Image.Resampling.LANCZOS)
        
        px = (width - sw) // 2
        py = (height - sh) // 2 - 20 - int(progress * 15)
        frame_img.paste(card_resized, (px, py), card_resized)
        
        draw_reticle(draw, px, py, px + sw, py + sh, color=(245, 158, 11, 200))
        
        if sf < 5:
            frame_img = apply_glitch(frame_img, magnitude=12)
            draw = ImageDraw.Draw(frame_img)
            
        draw_text_centered(draw, "SQUAD 02: INTEGRATION (CROSS-FUNCTIONAL)", 120, font_hud, (245, 158, 11, 255))
        draw_text_centered(draw, "KONG JIA LUNG", 580, font_subtitle, (255, 255, 255, 255))
        
    elif 360 <= f < 450:
        # Scene 4: Frontend Squad (Feng & Georgene) (90 frames / 3 seconds)
        sf = f - 360
        progress = sf / 90.0
        card1 = profiles["feng"]
        card2 = profiles["georgene"]
        cw, ch = card1.size
        
        scale = 1.0 + progress * 0.22
        sw, sh = int(cw * scale), int(ch * scale)
        card1_r = card1.resize((sw, sh), Image.Resampling.LANCZOS)
        card2_r = card2.resize((sw, sh), Image.Resampling.LANCZOS)
        
        gap = 60
        total_w = sw * 2 + gap
        start_x = (width - total_w) // 2
        py = (height - sh) // 2 - 20 + int(progress * 15)
        
        frame_img.paste(card1_r, (start_x, py), card1_r)
        frame_img.paste(card2_r, (start_x + sw + gap, py), card2_r)
        
        draw_reticle(draw, start_x, py, start_x + sw, py + sh, color=(16, 185, 129, 200))
        draw_reticle(draw, start_x + sw + gap, py, start_x + sw + gap + sw, py + sh, color=(16, 185, 129, 200))
        
        if sf < 5:
            frame_img = apply_glitch(frame_img, magnitude=12)
            draw = ImageDraw.Draw(frame_img)
            
        draw_text_centered(draw, "SQUAD 03: FRONTEND SQUAD", 120, font_hud, (52, 211, 153, 255))
        draw_text_centered(draw, "THOO CHIN FENG  |  GEORGENE WEE EE JERN", 580, font_subtitle, (255, 255, 255, 255))
        
    elif 450 <= f < 540:
        # Scene 5: 1 TEAM (Chris)
        sf = f - 450
        progress = sf / 90.0
        fade = min(1.0, (540 - f) / 15.0)
        card = profiles["chris"]
        cw, ch = card.size
        
        scale = 1.0 + progress * 0.25
        sw, sh = int(cw * scale), int(ch * scale)
        card_resized = card.resize((sw, sh), Image.Resampling.LANCZOS)
        
        px = (width - sw) // 2 + int(progress * 25)
        py = (height - sh) // 2 - 20 - int(progress * 15)
        frame_img.paste(card_resized, (px, py), card_resized)
        
        draw_reticle(draw, px, py, px + sw, py + sh, color=(52, 211, 153, 200))
        
        if sf < 5:
            frame_img = apply_glitch(frame_img, magnitude=12)
            draw = ImageDraw.Draw(frame_img)
            
        draw_text_centered(draw, "1 TEAM // PROJECT MANAGER", 120, font_hud, (52, 211, 153, int(255 * fade)))
        draw_text_centered(draw, "CHRIS WONG LIHONG", 580, font_subtitle, (255, 255, 255, int(255 * fade)))
        
    elif 540 <= f < 630:
        # Scene 6: 14 WEEK DELIVERY
        sf = f - 540
        progress = min(1.0, sf / 50.0)
        fade = min(1.0, (630 - f) / 15.0)
        pulse = 1.0 + math.sin(sf * 0.15) * 0.03
        pulse_font = ImageFont.truetype(font_bold_path, int(48 * pulse))
        
        draw_typewriter_text(draw, "14-WEEK DELIVERY", 300, pulse_font, progress, (239, 68, 68, int(255 * fade)))
        if sf > 25:
            sub_p = min(1.0, (sf - 25) / 30.0)
            draw_text_centered(draw, "THE COUNTDOWN HAS BEGUN", 390, font_subtitle, (148, 163, 184, int(255 * sub_p * fade)))
            
    elif 630 <= f < 720:
        # Scene 7: WORKING TOWARDS ONE GOAL
        sf = f - 630
        progress = min(1.0, sf / 50.0)
        fade = min(1.0, (720 - f) / 15.0)
        draw_typewriter_text(draw, "WORKING TOWARDS ONE GOAL...", 300, font_title, progress, (255, 255, 255, int(255 * fade)))
        
    elif 720 <= f < 900:
        # Scene 8: Climax - PURITYLOOP AI
        sf = f - 720
        progress = min(1.0, sf / 60.0)
        flashing_color = (255, 255, 255, 255)
        if 20 <= sf < 50:
            if (sf // 3) % 2 == 0:
                flashing_color = (239, 68, 68, 255)
                
        draw_text_centered(draw, "PURITYLOOP AI", 220, font_title, flashing_color)
        
        if sf > 25:
            sub_p = min(1.0, (sf - 25) / 35.0)
            draw_text_centered(draw, "Can this project be completed or not?", 330, font_subtitle, (255, 255, 255, int(255 * sub_p)))
            
        if sf > 55:
            final_p = min(1.0, (sf - 55) / 35.0)
            draw_text_centered(draw, "Stay tuned to find out!", 420, font_subtitle, (52, 211, 153, int(255 * final_p)))
            
    # Letterbox overlays
    draw.rectangle([0, 0, width, bar_h], fill=(0, 0, 0, 255))
    draw.rectangle([0, height - bar_h, width, height], fill=(0, 0, 0, 255))
    
    draw.text((30, height - 55), "CAPSTONE CINEMATICS", font=font_hud, fill=(71, 85, 105, 255))
    draw.text((width - 200, height - 55), f"T-00:{30 - (f//fps):02d} SEC", font=font_hud, fill=(71, 85, 105, 255))
    
    frame_rgb = frame_img.convert("RGB")
    frame_np = np.array(frame_rgb)
    frame_bgr = cv2.cvtColor(frame_np, cv2.COLOR_RGB2BGR)
    
    video_writer.write(frame_bgr)

video_writer.release()
print("Cinematic trailer visual video successfully written.")
