# Maintainer: Pierre-Loup A. Griffais <pgriffais@valvesoftware.com>

pkgname=gamescope
_srctag=3.15.11
pkgver=${_srctag//-/.}
pkgrel=1
pkgdesc="gaming shell based on Xwayland, powered by Vulkan and DRM"
arch=(x86_64)
url="https://github.com/ValveSoftware/gamescope"
license=('MIT')
depends=('xorg-xwayland' 'libavif' 'aom' 'rav1e' 'libxres' 'xcb-util-errors' 'freerdp' 'xcb-util-wm' 'libxcomposite' 'pixman' 'libinput' 'seatd' 'pipewire' 'libxmu' 'libxcursor' 'powerbuttond' 'libdecor' 'libei')
makedepends=(openssh git meson cmake wayland-protocols ninja glslang glm vulkan-headers benchmark)
source=("gamescope-session"
        "gamescope-wayland.desktop"
        "gamescope-mimeapps.list"
        "gamescope-session.service"
        "gamescope-portals.conf"
        "start-gamescope-session"
        "steam_http_loader.desktop"
        "steam-http-loader"
        "git+https://github.com/ValveSoftware/gamescope.git#tag=$_srctag"
        "git+https://github.com/Joshua-Ashton/wlroots.git"
        "git+https://gitlab.freedesktop.org/emersion/libliftoff.git"
        "git+https://github.com/Joshua-Ashton/GamescopeShaders.git#tag=v0.1"
        # FIXME Upstream gamescope is just selecting master branch at build time, so we are arbitrarily snapshotting a
        #       revision when bumping the version here such that the build is reproducible.
        "git+https://github.com/nothings/stb.git#commit=af1a5bc352164740c1cc1354942b1c6b72eacb8a")
sha256sums=('6048e912c1710c3187bcad67efe1abf5f6aaf66bfab8f7a1660b400f3f1378ec'
            'fe515fce8f151a6c03a89e043044bfddf8cd6ee89027d2cfbcf6f6706c78ca76'
            'e37ba6107f3a84cf47c2799b537a88583e6cb8951167a9c6a48fa1d85996206b'
            '8e31e370bc644c470483aec4d4b86cd22e7bede48af70a330b1d912500831fc2'
            'b74f4515a3ed793973b3be6eca145d7ba862dbf50218c694fb478ba725bfd025'
            'beabd15da2a15ef22c20de2be3b023029254d93c55784e628928ec0324ffe1b7'
            '525060896abef2da9db8d8294253b7444d60e48cf6cc0496ca48fc7084cc8590'
            'dea09abb47c3d907c00ff7f36967b599f3caca554ac6eb7b7dc6d2d78651dd44'
            'SKIP'
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
	git -c protocol.file.allow=always submodule update

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

	# portals
	install -D -m 644 gamescope-portals.conf "$pkgdir"/usr/share/xdg-desktop-portal/gamescope-portals.conf

	install -d "$pkgdir"/usr/share/gamescope/reshade
	cp -r "$srcdir"/GamescopeShaders/* "$pkgdir"/usr/share/gamescope/reshade/
	chmod -R 655 "$pkgdir"/usr/share/gamescope

	cd "$pkgname/build"

	DESTDIR="$pkgdir" meson install --skip-subprojects

	rm -rf "$pkgdir"/usr/include
	rm -rf "$pkgdir"/usr/lib/libwlroots*
	rm -rf "$pkgdir"/usr/lib/pkgconfig
}
