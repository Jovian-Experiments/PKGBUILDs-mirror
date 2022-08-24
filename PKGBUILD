# Maintainer: Antonin Décimo <antonin dot decimo at gmail dot com>
# Contributor: AndyRTR <andyrtr@archlinux.org>

pkgname=xorg-xwayland-jupiter
pkgver=jupiter.20220824.1d653e264
_tag=jupiter-20220824
pkgrel=1
arch=('x86_64')
license=('custom')
groups=('xorg')
url="https://xorg.freedesktop.org"
pkgdesc="Run X clients under Wayland (git version)"
depends=('nettle' 'libegl' 'libepoxy' 'systemd-libs' 'libxfont2'
         'pixman' 'xorg-server-common' 'libxcvt')
makedepends=('meson' 'git' 'openssh'
             'xorgproto' 'xtrans'
             'pixman' 'libxkbfile' 'libxfont2' 'dbus'
             'xorg-font-util'
             'wayland' 'wayland-protocols'
             'libdrm' 'libepoxy'
             'systemd'
             'egl-wayland'
)
source=("xserver-jupiter::git+ssh://git@gitlab.steamos.cloud/jupiter/xserver.git#tag=$_tag")
sha256sums=('SKIP')
provides=('xorg-xwayland' 'xorg-server-xwayland' 'xorg-server-xwayland-jupiter')
conflicts=('xorg-xwayland' 'xorg-server-xwayland' 'xorg-server-xwayland-jupiter')
replaces=('xorg-server-xwayland-jupiter')

pkgver() {
  cd xserver-jupiter
  local head=$(git rev-parse --short HEAD)
  printf "%s.%s" "${_tag//-/.}" "$head"
}

build() {
  # Since pacman 5.0.2-2, hardened flags are now enabled in makepkg.conf
  # With them, module fail to load with undefined symbol.
  # See https://bugs.archlinux.org/task/55102 / https://bugs.archlinux.org/task/54845
#  export CFLAGS=${CFLAGS/-fno-plt}
#  export CXXFLAGS=${CXXFLAGS/-fno-plt}
#  export LDFLAGS=${LDFLAGS/,-z,now}

  arch-meson xserver-jupiter build \
    -D ipv6=true \
    -D xvfb=false \
    -D xnest=false \
    -D xcsecurity=true \
    -D xorg=false \
    -D xephyr=false \
    -D xwayland=true \
    -D xwayland_eglstream=true \
    -D xwin=false \
    -D xquartz=false \
    -D glamor=true \
    -D udev=true \
    -D systemd_logind=true \
    -D suid_wrapper=true \
    -D xkb_dir=/usr/share/X11/xkb \
    -D xkb_output_dir=/var/lib/xkb

  # Print config
  meson configure build
  ninja -C build
}

package() {

  # bin + manpage + .pc file
  install -m755 -Dt "${pkgdir}"/usr/bin build/hw/xwayland/Xwayland
  install -m644 -Dt "${pkgdir}"/usr/share/man/man1 build/hw/xwayland/Xwayland.1
  install -m644 -Dt "${pkgdir}"/usr/lib/pkgconfig build/hw/xwayland/xwayland.pc

  # license
  install -m644 -Dt "${pkgdir}/usr/share/licenses/${pkgname}" xserver-jupiter/COPYING
}
