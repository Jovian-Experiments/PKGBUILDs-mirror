# Maintainer: Pierre-Loup A. Griffais <pgriffais@valvesoftware.com>

pkgname=gamescope
_srctag=3.11.52-beta4
pkgver=${_srctag//-/.}
pkgrel=1
pkgdesc="gaming shell based on Xwayland, powered by Vulkan and DRM"
arch=(x86_64)
url="https://github.com/Plagman/gamescope"
license=('MIT')
depends=('xorg-xwayland-jupiter' 'libxres' 'xcb-util-errors' 'freerdp' 'xcb-util-wm' 'libxcomposite' 'pixman' 'libinput' 'seatd' 'pipewire' 'libxmu')
makedepends=(git meson cmake wayland-protocols ninja glslang vulkan-headers)
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
sha256sums=('0e5d16abc2ec2c304ebc72254be3b70ab96c985b1e0f9c4cb416b4c61e10f0b4'
            'fe515fce8f151a6c03a89e043044bfddf8cd6ee89027d2cfbcf6f6706c78ca76'
            'e37ba6107f3a84cf47c2799b537a88583e6cb8951167a9c6a48fa1d85996206b'
            '281d892e32c2c31e9df94c5e712a1fde46c0a2f3214aa2df5b7253c6db47977c'
            'beabd15da2a15ef22c20de2be3b023029254d93c55784e628928ec0324ffe1b7'
            '525060896abef2da9db8d8294253b7444d60e48cf6cc0496ca48fc7084cc8590'
            'dea09abb47c3d907c00ff7f36967b599f3caca554ac6eb7b7dc6d2d78651dd44'
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

	cd "$pkgname/build"

	DESTDIR="$pkgdir" meson install --skip-subprojects

	rm -rf "$pkgdir"/usr/include
	rm -rf "$pkgdir"/usr/lib/libwlroots*
	rm -rf "$pkgdir"/usr/lib/pkgconfig
}
