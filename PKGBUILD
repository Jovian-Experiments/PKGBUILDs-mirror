# Maintainer: Pierre-Loup A. Griffais <pgriffais@valvesoftware.com>

pkgname=gamescope
_srctag=3.16.15
pkgver=${_srctag//-/.}
pkgrel=3
pkgdesc="gaming shell based on Xwayland, powered by Vulkan and DRM"
arch=(x86_64)
url="https://github.com/ValveSoftware/gamescope"
license=('MIT')
depends=('xorg-xwayland' 'libavif' 'aom' 'rav1e' 'libxres' 'xcb-util-errors' 'freerdp' 'xcb-util-wm' 'libxcomposite' 'pixman' 'libinput' 'seatd' 'pipewire' 'libxmu' 'libxcursor' 'libdecor' 'libei' 'luajit')
makedepends=(openssh git meson cmake wayland-protocols ninja glslang glm vulkan-headers benchmark)
source=("galileo-mura-setup.service"
        "gamescope-session"
        "gamescope-wayland.desktop"
        "gamescope-mimeapps.list"
        "gamescope-session.service"
        "gamescope-session.target"
        "gamescope-portals.conf"
        "gamescope-xbindkeys.service"
        "gamescope-mangoapp.service"
        "ibus-gamescope.service"
        "start-gamescope-session"
        "steam-launcher"
        "steam-launcher.service"
        "steam-notif-daemon.service"
        "steam-short-session-tracker"
        "steam_http_loader.desktop"
        "steam-http-loader"
        "git+https://github.com/ValveSoftware/gamescope.git#tag=$_srctag"
        "git+https://github.com/Joshua-Ashton/wlroots.git"
        "git+https://gitlab.freedesktop.org/emersion/libliftoff.git"
        "git+https://github.com/Joshua-Ashton/GamescopeShaders.git#tag=v0.1"
        # FIXME Upstream gamescope is just selecting master branch at build time, so we are arbitrarily snapshotting a
        #       revision when bumping the version here such that the build is reproducible.
        "git+https://github.com/nothings/stb.git#commit=af1a5bc352164740c1cc1354942b1c6b72eacb8a"
        "git+https://github.com/g-truc/glm.git#commit=0af55ccecd98d4e5a8d1fad7de25ba429d60e863")
sha256sums=('941f5a16a495c9c4de0302819c0069749db6915345ac1e207a12544863391e4b'
            '8a9886a96a321efef5e2c928cf2e54a075b72ea37b2d12e8412fd2459f4775f2'
            'fe515fce8f151a6c03a89e043044bfddf8cd6ee89027d2cfbcf6f6706c78ca76'
            'e37ba6107f3a84cf47c2799b537a88583e6cb8951167a9c6a48fa1d85996206b'
            'e4add84152c3c0dfa53cf6bd2a1f15c2ce74d2312f7fa945b9476e91c8752544'
            'ce7e26d4145b44a1161d8ec050fb97f3c8786b7c5b719f36aa1dfb984b5863c1'
            'eae6b5cbd0735d6732c8b7de99ed3362f24f6aa76bbba0950a14b99040f4e6d0'
            'd9a8e593bea8ea0afc96cec3849c48e87b686d263a5d7a09a272237cc35acb52'
            '81da49a733a757a4848a5c95011c3f9d3e584373244722ed9b26687ae0126793'
            'd010a36f52f2122b51f8a0bdc983560a553759f85c2eb5a9ccb2b1a6de367059'
            '10462d319e9d2a97a8fc9265628c03819bd6fd86dc13cee6e38151fc9b270407'
            'bc2e16bbff2357091f04b7049b9fa40d3fc8d75e909c09310ebe39acc5c09621'
            'f92f193a541d9bdb94e312be7922257e72cf4bb08a0f0bec8d4222e561118aec'
            '609da4097f9addc83f07647cc6e5c75493ddc8372853868c033d1c71c5c0cce9'
            '674367927b9d0665a1e1c57ebcd7373683659b1dc1020d2bffd4ab50e4af73fa'
            '525060896abef2da9db8d8294253b7444d60e48cf6cc0496ca48fc7084cc8590'
            'f57fcba25b211381a9402d3d0c4723301afaef185e9ecffc75839e5af2aee4c8'
            'e41df706604e97715a509222e3a839c7b10fd83f0746e1ab0a3a387fde091599'
            'SKIP'
            'SKIP'
            '03726f2fb44ae79e6a398e8f9aaaf8054800dda9b8298726157522fe5f7296b1'
            'e39e0c91b297bfd707afcda84ecdc15a08c22e2ad4c347fc3533b1ed98fb3f85'
            '85f3e55fb527e9853bd4fc31300253587198831660a743eaa55f6b40fe1b9c90')

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

	rm -rf subprojects/glm
	git clone "$srcdir/glm" subprojects/glm
	cp -av subprojects/packagefiles/glm/* subprojects/glm/ # patch from the .wrap we elided
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
	install -D -m 755 gamescope-session "$pkgdir"/usr/lib/steamos/gamescope-session
	install -D -m 755 steam-launcher "$pkgdir"/usr/lib/steamos/steam-launcher
  install -D -m 755 steam-short-session-tracker "$pkgdir"/usr/lib/steamos/steam-short-session-tracker

	install -D -m 755 start-gamescope-session "$pkgdir"/usr/bin/start-gamescope-session
	install -D -m 644 gamescope-wayland.desktop "$pkgdir"/usr/share/wayland-sessions/gamescope-wayland.desktop

	# url handling
	install -D -m 644 steam_http_loader.desktop "$pkgdir"/usr/share/applications/steam_http_loader.desktop
	install -D -m 644 gamescope-mimeapps.list "$pkgdir"/usr/share/applications/gamescope-mimeapps.list
	install -D -m 755 steam-http-loader "$pkgdir"/usr/bin/steam-http-loader

	# systemd
	install -D -m 644 galileo-mura-setup.service "$pkgdir"/usr/lib/systemd/user/galileo-mura-setup.service
	install -D -m 644 gamescope-session.service "$pkgdir"/usr/lib/systemd/user/gamescope-session.service
	install -D -m 644 gamescope-session.target "$pkgdir"/usr/lib/systemd/user/gamescope-session.target
	install -D -m 644 gamescope-mangoapp.service "$pkgdir"/usr/lib/systemd/user/gamescope-mangoapp.service
	install -D -m 644 ibus-gamescope.service  "$pkgdir"/usr/lib/systemd/user/ibus-gamescope.service
	install -D -m 644 steam-launcher.service "$pkgdir"/usr/lib/systemd/user/steam-launcher.service
	install -D -m 644 steam-notif-daemon.service "$pkgdir"/usr/lib/systemd/user/steam-notif-daemon.service
	install -D -m 644 gamescope-xbindkeys.service "$pkgdir"/usr/lib/systemd/user/gamescope-xbindkeys.service

	# portals
	install -D -m 644 gamescope-portals.conf "$pkgdir"/usr/share/xdg-desktop-portal/gamescope-portals/gamescope-portals.conf

	install -d "$pkgdir"/usr/share/gamescope/reshade
	cp -r "$srcdir"/GamescopeShaders/* "$pkgdir"/usr/share/gamescope/reshade/
	chmod -R 655 "$pkgdir"/usr/share/gamescope

	cd "$pkgname/build"

	DESTDIR="$pkgdir" meson install --skip-subprojects

	rm -rf "$pkgdir"/usr/include
	rm -rf "$pkgdir"/usr/lib/libwlroots*
	rm -rf "$pkgdir"/usr/lib/pkgconfig
}
