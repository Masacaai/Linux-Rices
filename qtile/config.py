#  __  __           _____ 
# |  \/  |   /\    / ____|   Github: https://www.github.com/Masacaai
# | \  / |  /  \  | (___  
# | |\/| | / /\ \  \___ \ 
# | |  | |/ ____ \ ____) |
# |_|  |_/_/    \_\_____/ 
#
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Modified by Masacaai 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.SOFTWARE

import os
import subprocess
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook, pangocffi
from libqtile.config import Click, Drag, Group, Key, Screen, Match, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import base

############
# DEFAULTS #
############

mod = "mod1"
terminal = guess_terminal()
last_focus = None
opacity_var = 0.8
red = 'e54252'
green = '2de564'
purple = '9535f4'
pink = 'e853ca'
blue = '4e49ed'
orange = 'e58342'
yellow = 'edcc49'
cyan = '49daed'  
bubblegum = 'fe14a9'
white = 'ffffff'

#############	
# FUNCTIONS #
#############

def change_transparency(window):
    """change window transparency based on his name/type."""    
    
    kls = window.window.get_wm_class()[1].lower()
    if window.window.get_wm_icon_name() == 'Picture-in-Picture' or 'mpv' in kls:
    	window.cmd_opacity(1)
    else:
    	window.cmd_opacity(opacity_var)
        
#########
# HOOKS #
#########
@hook.subscribe.startup_once
def autostart_once():
    home = os.path.expanduser('~/.config/qtile/autostart_once.sh')
    subprocess.call([home])

# @hook.subscribe.startup
# def autostart():
#   home = os.path.expanduser('~/.config/qtile/autostart.sh')
#   subprocess.call([home])
    
@hook.subscribe.client_new
def transparent_window(window):
    """Make new windows a little transparent."""
    change_transparency(window)
            
@hook.subscribe.client_focus
def client_focus(window):
    """Change transparency on focus."""
    global last_focus

    if last_focus is not None and last_focus != window:
        try:
            change_transparency(last_focus)
        except Exception:
            pass  # ignore if error

    if last_focus != window:
        last_focus = window
        window.cmd_opacity(1)  # current focused window: no transp
        
@lazy.function
def float_to_front(qtile):
    logging.info("bring floating windows to front")
    for group in qtile.groups:
        for window in group.windows:
            if window.floating:
                window.cmd_bring_to_front()


################
# KEY BINDINGS #
################
keys = [
	    
	    ##################
	    # QTILE CONTROLS #
	    ##################
	    
	    Key([mod], "h", 
	    lazy.layout.left(), 
	    desc="Shift focus left"),
	    
	    Key([mod], "l", 
	    lazy.layout.right(),
	    desc="Shift focus right"),
	    
	    Key([mod], "j", 
	    lazy.layout.down(),
	    desc="Shift focus down"),
	    
	    Key([mod], "k", 
	    lazy.layout.up(),
	    desc="Shift focus up"),
	    
	    Key([mod, "shift"], "h", 
	    lazy.layout.swap_left(),
	    desc="Shift window left"),
	    
	    Key([mod, "shift"], "l", 
	    lazy.layout.swap_right(),
	    desc="Shift window right"),
	    
	    Key([mod, "shift"], "j", 
	    lazy.layout.shuffle_down(),
	    desc="Shift window down"),
	    
	    Key([mod, "shift"], "k", 
	    lazy.layout.shuffle_up(),
	    desc="Shift window up"),
	    
	    Key([mod], "i", 
	    lazy.layout.grow(),
	    desc="Grow focused window"),
	    
	    Key([mod], "m", 
	    lazy.layout.shrink(),
	    desc="Shrink focused window"),
	    
	    Key([mod], "n", 
	    lazy.layout.normalize(),
	    desc="Normalize window sizes"),
	    
	    Key([mod], "o", 
	    lazy.layout.maximize(),
	    desc="Maximise current window size"),
	    
	    Key([mod, "shift"], "space", 
	    lazy.layout.flip(),
	    desc="Flip left and right panes of windows"),
	    
	    Key([mod], "Tab", 
	    lazy.next_layout(), 
	    desc="Toggle between layouts"),
	    
	    Key([mod], "q", 
	    lazy.window.kill(), 
	    desc="Kill focused window"),
	    
	    Key([mod, "shift"], "r", 
	    lazy.restart(), 
	    desc="Restart qtile"),
	    
	    Key([mod, "shift"], "e", 
	    lazy.shutdown(), 
	    desc="Shutdown qtile"),
	    
	    Key([mod, "shift"], "f", 
	    lazy.window.toggle_floating(), 
	    desc='toggle floating'),
	    
	    ###################
	    # SYSTEM CONTROLS #
	    ###################
	    Key([], "XF86AudioRaiseVolume", 
	    lazy.spawn("pulseaudio-ctl up"), 
	    desc="Raises volume"),
	    
	    Key([], "XF86AudioLowerVolume", 
	    lazy.spawn("pulseaudio-ctl down"), 
	    desc="Lowers volume"),
	    
	    Key([], "XF86AudioMute", 
	    lazy.spawn("pulseaudio-ctl mute"), 
	    desc="Mutes audio"),
	    
	    Key([], "XF86AudioPlay", 
	    lazy.spawn("playerctl play"), 
	    desc="Pause/Play audio"),
	    
	    Key([], "XF86AudioNext", 
	    lazy.spawn("playerctl next"), 
	    desc="Next track"),
	    
	    Key([], "XF86AudioPrev", 
	    lazy.spawn("playerctl previous"), 
	    desc="Previous track"),
	    
	    Key([], "XF86MonBrightnessUp", 
	    lazy.spawn("xbacklight -inc 10"), 
	    desc="Increase brightness"),
	    
	    Key([], "XF86MonBrightnessDown", 
	    lazy.spawn("xbacklight -dec 10"), 
	    desc="Decrease brightness"),
	    
	    Key(["mod4"], "l", 
	    lazy.spawn("betterlockscreen -l -t 'Non ducor, duco.'"),
	    desc="Lock screen"),
            
            Key([mod], "space",
            lazy.hide_show_bar(),
            desc="Toggle bar visibility"),

            Key(["mod4","shift"], "f",
            float_to_front,
            desc="Brings all floating windows to front"),
	    ######################
	    # START APPLICATIONS #
	    ######################
	    Key([mod], "Return", 
	    lazy.spawn(terminal), 
	    desc="Launch terminal"),
	    
	    KeyChord(["mod4"], "r", [
                Key(["mod4"], "r",
                lazy.spawn("rofi -show run"),
                desc="Launch Rofi Run"),

                Key(["mod4"], "f",
                lazy.spawn("rofi -show file-browser-extended"),
                desc="Launch Rofi File Browser"),

                Key(["mod4"], "s",
                lazy.spawn("/home/masacaai/.scripts/rofi/rofis.sh"),
                desc="Launch Rofi Search"),

                Key(["mod4"], "w",
                lazy.spawn("ytfzf -D"),
                desc="Launch Rofi Watch"),

            ]),
	    
	    Key([mod], "w", 
	    lazy.spawn("qutebrowser"), 
	    desc="Launch qutebrowser"),

	    Key([mod], "f",
	    lazy.spawn("firefox"),
	    desc="Launch firefox"),

	    Key([mod], "r",
	    lazy.spawn("kitty -e ranger"),
	    desc="Launch ranger"),
	    
	    Key([mod], "p", 
	    lazy.spawn("pcmanfm"), 
	    desc="Launch pcmanfm"),
	    
	    Key([mod], "t", 
	    lazy.spawn("pkill picom"), 
	    desc="Kill picom instance"),
	    
	    Key([mod, "control"], "t", 
	    lazy.spawn("picom -b -f --experimental-backends"), 
	    desc="Launch picom instance"),
	    
            Key([mod], "Print", 
	    lazy.spawn("/home/masacaai/.scripts/maim/sc.sh"), 
	    desc="Desktop Screenshot"),
	    
	    Key([], "Print", 
	    lazy.spawn("/home/masacaai/.scripts/maim/scs.sh"), 
	    desc="Area screenshot"),
	    
	    Key([mod, "control"], "x", 
	    lazy.spawn("xkill"), 
	    desc="Launch xkill"),
	    
	    Key([mod], "z", 
	    lazy.spawn("zettlr"), 
	    desc="Launches Zettlr"),
	    
	    Key([mod], "backslash", 
	    lazy.spawn("code"), 
	    desc="Launch Code-OSS"),
	    
	    Key(["mod4"], "s", 
	    lazy.spawn("signal-desktop"), 
	    desc="Launch Signal"),
	   
            Key([mod], "v",
            lazy.spawn("kitty -e nvim"),
            desc="Launch Neovim"),

	    Key(["mod4"], "n", 
	    lazy.spawn("kitty -e newsboat"), 
	    desc="Launch Newsboat"),

	    Key(["mod4"], "v", 
	    lazy.spawn("VirtualBox"), 
	    desc="Launch VirtualBox"),

            Key(["mod4"], "t",
            lazy.spawn("urxvt -e ssh masacaai@tilde.club"),
            desc="Launch Tilde.Club"),

	    Key(["mod4"], "c",
	    lazy.spawn("kitty -e nvim .config/qtile/config.py"),
	    desc="Launch configfile"),

	]
##########
# GROUPS #
########## 

'''
groups = [
	Group("1", label='GEN', matches=[Match(wm_class=["firefox"])]),
	Group("2", label='DEV', matches=[Match(wm_class=["zathura"])]),
	Group("3", label='CHT', matches=[Match(wm_class=["discord"])]),
	Group("4", label='SYS', matches=[Match(wm_class=["ranger"])]),
	Group("5", label='MUS', matches=[Match(wm_class=["spotify"])]),
]

'''

groups = [Group(i,label='', layout = 'monadtall') for i in "1234567890"]


for i in groups:
    keys.extend([
		
		Key([mod], i.name, 
		lazy.group[i.name].toscreen(), 
		desc="Switch to group {}".format(i.name)),
		
		Key([mod, "shift"], i.name, 
		lazy.window.togroup(i.name, switch_group=True), 
		desc="Switch to & move focused window to group {}".format(i.name)),
		    		
    		])



###########
# LAYOUTS #
###########
layouts = [
	    # layout.Max(),
	    # layout.Floating(),
	    layout.MonadTall(
	    			border_width=2,
	    			single_border_width=0,
	    			border_focus=white,
	    			border_normal=white,
	    			single_margin=0,
	    			margin=10,
				
	    		     ),
	    # layout.Zoomy(),
	    # layout.Stack(num_stacks=2),
	    layout.Bsp(
	    			border_width=2,
	    			single_border_width=0,
	    			border_focus=white,
	    			border_normal=white,
	    			single_margin=0,
	    			margin=10,
	    			
	    		),
	    # layout.Columns(),
	    # layout.Matrix(),
	    layout.MonadWide(
	    			border_width=2,
	    			single_border_width=0,
	    			border_focus=white,
	    			border_normal=white,
	    			single_margin=0,
	    			margin=10,
	    			
	    		     ),
	    # layout.RatioTile(),
	    # layout.Tile(),
	    # layout.TreeTab(),
	    # layout.VerticalTile(),
	  ]

###########
# DISPLAY #
###########
widget_defaults = dict(
		    font='sans',
		    fontsize=20,
		    padding=1,
                    foreground='#020013',
                    background= '#020013'
		       )

extension_defaults = widget_defaults.copy()

screens = [
	    Screen(
			bottom=bar.Bar(
				    [
#					widget.TextBox("   " ),
                                        widget.CurrentLayoutIcon(
                                                                    scale = 0.8,
                                                                    background = bubblegum,
                                                                ),
                                        widget.GroupBox(
							highlight_method='line', 
                                                        highlight_color= [bubblegum,bubblegum],
                                                        block_highlight_text_color= cyan,
                                                        inactive = '#020013',
							this_current_screen_border= bubblegum,
							urgent_alert_method = 'text', 
							urgent_border = yellow, 
							urgent_text = yellow,
                                                        background = bubblegum,
							),
#					widget.CurrentLayoutIcon(scale = 0.8),
					widget.TextBox(text='◣', background='#020013', foreground=bubblegum, padding = -1, fontsize=56),
					widget.WindowName(
                                                            foreground = bubblegum,
                                                            empty_group_string = 'Arch Qtile',
                                                            format = '{class}',
                                                            #max_chars = 45,
                                                            ),
				        widget.Spacer(),
					widget.Systray(),
                                        widget.TextBox(text='◢', background='#020013', foreground=cyan, padding = -1, fontsize=56),
					widget.TextBox(" ", background=cyan, padding=2),
					widget.PulseVolume(background=cyan),		 
					widget.TextBox(text='◢', background=cyan, foreground=yellow, padding = -1, fontsize=56),
					widget.Backlight(
							  format='☀ {percent:2.0%}',
							  max_brightness_file='/sys/class/backlight/intel_backlight/max_brightness',
							  brightness_file='/sys/class/backlight/intel_backlight/brightness',
							  background= yellow ,  
							 ),
					widget.TextBox(text='◢', background=yellow, foreground=orange, padding = -1, fontsize=56),
					widget.CPU(
							  format='CPU {load_percent}%',
							  background= orange ,
						   ),
					widget.TextBox(text='◢', background=orange, foreground=blue, padding = -1, fontsize=56),
					widget.Memory(
                                                          format='RAM {MemUsed: .0f}{mm}',
							  background= blue ,
						      ),
					widget.TextBox(text='◢', background=blue, foreground=red, padding = -1, fontsize=56),
					widget.DF(
							  visible_on_warn=False,
							  format=' {uf}{m}',
							  background= red ,
					          ),
					widget.TextBox(text='◢', background=red, foreground=pink, padding = -1, fontsize=56),
					widget.Clock(
							  format=' %d-%m %a',
							  background= pink ,
						     ),
					widget.TextBox(text='◢', background=pink, foreground=purple, padding = -1, fontsize=56),
					widget.Clock(
							  format=' %I:%M %p',
							  background= purple ,  
						     ),
					widget.TextBox(text='◢', background=purple, foreground=green, padding = -1, fontsize=56),
					widget.Wlan(
							  format='   {percent:2.0%}',
							  background= green ,
							  
						    ),
					widget.TextBox(text='◢', background=green, foreground=white, padding = -1, fontsize=56),
					widget.Battery(
                                                          format='  {percent:2.0%}',
                                                          background= white
                                                    ),
				    ],
				    30,
				   ),
			wallpaper="~/Pictures/Wallpapers/wallpaper.png",
                        wallpaper_mode="fill"
	    	   ),
	  ]

#########
# MOUSE #
#########
mouse = [
	    Drag([mod], "Button1", lazy.window.set_position_floating(),
		 start=lazy.window.get_position()),
	    Drag([mod], "Button3", lazy.window.set_size_floating(),
		 start=lazy.window.get_size()),
	    Click([mod], "Button2", lazy.window.bring_to_front())
	]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(	
					
					border_width=2,
                                        border_focus=white,
                                        border_normal=white,
#					float_rules=[
#    
#	    						    {'wmclass': 'confirm'},
#							    {'wmclass': 'dialog'},
#							    {'wmclass': 'download'},
#							    {'wmclass': 'error'},
#							    {'wmclass': 'file_progress'},
#							    {'wmclass': 'notification'},
#							    {'wmclass': 'splash'},
#							    {'wmclass': 'toolbar'},
#							    {'wmclass': 'confirmreset'},  # gitk
#							    {'wmclass': 'makebranch'},  # gitk
#							    {'wmclass': 'maketag'},  # gitk
#							    {'wname': 'branchdialog'},  # gitk
#							    {'wname': 'pinentry'},  # GPG key password entry
#							    {'wmclass': 'ssh-askpass'},  # ssh-askpass
#						    ]
				  )	

auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


