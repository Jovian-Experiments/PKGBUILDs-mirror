# Maintainer: Pierre-Loup A. Griffais <pgriffais@valvesoftware.com>

pkgname=gamescope
_srctag=3.11.47
pkgver=${_srctag//-/.}
pkgrel=5
pkgdesc="gaming shell based on Xwayland, powered by Vulkan and DRM"
arch=(x86_64)
url="https://github.com/Plagman/gamescope"
license=('MIT')
depends=('xorg-xwayland-jupiter' 'libxres' 'xcb-util-errors' 'freerdp' 'xcb-util-wm' 'libxcomposite' 'pixman' 'libinput' 'seatd' 'pipewire')
makedepends=(git meson wayland-protocols ninja glslang vulkan-headers)
source=("gamescope-session"
        "gamescope-wayland.desktop"
        "gamescope-mimeapps.list"
        "gamescope-session.service"
        "start-gamescope-session"
        "steam_http_loader.desktop"
        "steam-http-loader"
        "git+https://github.com/Plagman/gamescope.git#tag=$_srctag"
        "git+https://gitlab.freedesktop.org/wlroots/wlroots.git"
        "git+https://gitlab.freedesktop.org/emersion/libliftoff.git"
        # FIXME Upstream gamescope is just selecting master branch at build time, so we are arbitrarily snapshotting a
        #       revision when bumping the version here such that the build is reproducible.
        "git+https://github.com/nothings/stb.git#commit=af1a5bc352164740c1cc1354942b1c6b72eacb8a")
sha256sums=('1ccc732c5369613f750e9a7f10b199bd2c4dc2f70a48af44154b301697fb48e1'
            'fe515fce8f151a6c03a89e043044bfddf8cd6ee89027d2cfbcf6f6706c78ca76'
            '0661f81cb268c7f4452534eb1ae59620b9311061a7d45c2d7eef4a5b8bc9666d'
            '01eff0f21fcfcc26ad6efdc8291eb771eb81f07eec2723571954294fba50af32'
            '2dbfae36a05044dbe931762203003e0aa4e3d883518f737f9af7b8979fc2104b'
            '525060896abef2da9db8d8294253b7444d60e48cf6cc0496ca48fc7084cc8590'
            'e55f8f2ca167ce3c4615d2e423f7eb6ed02019e37e0bbaa3b050a85b25468849'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

install=gamescope.install

prepare() {
	cd "$pkgname"

	# git submodules
	git submodule init
	git config submodule.subprojects/wlroots.url "$srcdir/wlroots"
	git config submodule.subprojects/libliftoff.url "$srcdir/libliftoff"
	git submodule update

	# meson subprojects
	rm -rf subprojects/stb
	git clone "$srcdir/stb" subprojects/stb
	cp -av subprojects/packagefiles/stb/* subprojects/stb/ # patch from the .wrap we elided
}

build() {
	cd "$pkgname"

	rm -rf build
	mkdir build
	cd build
	arch-meson --buildtype release --prefix /usr ..
	ninja
}

package() {
	install -D -m 755 gamescope-session "$pkgdir"/usr/bin/gamescope-session
	install -D -m 755 start-gamescope-session "$pkgdir"/usr/bin/start-gamescope-session
	install -D -m 644 gamescope-wayland.desktop "$pkgdir"/usr/share/wayland-sessions/gamescope-wayland.desktop

	# url handling
	install -D -m 644 steam_http_loader.desktop "$pkgdir"/usr/share/applications/steam_http_loader.desktop
	install -D -m 644 gamescope-mimeapps.list "$pkgdir"/usr/share/applications/gamescope-mimeapps.list
	install -D -m 755 steam-http-loader "$pkgdir"/usr/bin/steam-http-loader

	install -D -m 644 gamescope-session.service "$pkgdir"/usr/lib/systemd/user/gamescope-session.service

	cd "$pkgname/build"

	DESTDIR="$pkgdir" meson install --skip-subprojects

	rm -rf "$pkgdir"/usr/include
	rm -rf "$pkgdir"/usr/lib/libwlroots*
	rm -rf "$pkgdir"/usr/lib/pkgconfig
}
