# Maintainer: Pierre-Loup A. Griffais <pgriffais@valvesoftware.com>

pkgname=gamescope
_srctag=3.11.24-beta
pkgver=${_srctag//-/.}
pkgrel=1
pkgdesc="gaming shell based on Xwayland, powered by Vulkan and DRM"
arch=(x86_64)
url="https://github.com/Plagman/gamescope"
license=('MIT')
depends=('xorg-xwayland-jupiter' 'libxres' 'xcb-util-errors' 'freerdp' 'xcb-util-wm' 'libxcomposite' 'pixman' 'libinput' 'seatd' 'pipewire')
makedepends=(git meson wayland-protocols ninja glslang vulkan-headers)
source=("gamescope-session"
        "gamescope-wayland.desktop"
        "gamescope-mimeapps.list"
        "steam_http_loader.desktop"
        "steam-http-loader"
        "git+https://github.com/Plagman/gamescope.git#tag=$_srctag"
        "git+https://gitlab.freedesktop.org/wlroots/wlroots.git"
        "git+https://gitlab.freedesktop.org/emersion/libliftoff.git"
        # FIXME Upstream gamescope is just selecting master branch at build time, so we are arbitrarily snapshotting a
        #       revision when bumping the version here such that the build is reproducible.
        "git+https://github.com/nothings/stb.git#commit=af1a5bc352164740c1cc1354942b1c6b72eacb8a")
sha256sums=('f7bd9c1842721218377e29cca48dbb9a5876a2ba1dade49b15721028bc3a324d'
            '9e36028b3459f4566b2d6a469f96728aaea8b9f9ea6e205b03d464c8077bd68c'
            'd81ff0942863e055d7ccf81c6568fda7f0eb6dcb4f87ee00350a674282d14841'
            '525060896abef2da9db8d8294253b7444d60e48cf6cc0496ca48fc7084cc8590'
            '713a724a88776156d2926ad4815a2d24e5d0e5f4b36833651e6fbc8d41476a98'
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
	install -D -m 644 gamescope-wayland.desktop "$pkgdir"/usr/share/wayland-sessions/gamescope-wayland.desktop

	# url handling
	install -D -m 644 steam_http_loader.desktop "$pkgdir"/usr/share/applications/steam_http_loader.desktop
	install -D -m 644 gamescope-mimeapps.list "$pkgdir"/usr/share/applications/gamescope-mimeapps.list
	install -D -m 755 steam-http-loader "$pkgdir"/usr/bin/steam-http-loader

	cd "$pkgname/build"

	DESTDIR="$pkgdir" meson install --skip-subprojects

	rm -rf "$pkgdir"/usr/include
	rm -rf "$pkgdir"/usr/lib/libwlroots*
	rm -rf "$pkgdir"/usr/lib/pkgconfig
}
