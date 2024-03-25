# Maintainer: Morten Linderud <foxboron@archlinux.org>
# Maintainer: David Runge <dvzrv@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Maintainer (Holo): Alberto Garcia <berto@igalia.com>

pkgbase=podman
pkgname=podman
pkgver=4.9.3
_commit=bd1b4a96544e6199f369feef8cb19c2e8f803b1f	#refs/tags/v4.9.3
pkgrel=1.2 # Holo: build only podman and not podman-docker, disable PGP signature
pkgdesc='Tool and library for running OCI-based containers in pods'
arch=(x86_64)
url='https://github.com/containers/podman'
license=(Apache-2.0)
makedepends=(
  apparmor
  btrfs-progs
  catatonit
  device-mapper
  git
  go
  go-md2man
  gpgme
  libseccomp
  systemd
)
# https://github.com/containers/podman/issues/13297
options=(!lto)
# Holo: disable PGP signature check until we have a patched pacman
# https://gitlab.archlinux.org/pacman/pacman/-/issues/92
# https://gitlab.archlinux.org/archlinux/packaging/packages/pacman/-/merge_requests/9
source=(
  git+$url#tag=$_commit
  $pkgname-4.6.0-defaultinitpath.patch
)
# See the release-keys repository
# https://github.com/containers/release-keys
validpgpkeys=(
  B7DBDCA456F7335E91F1C25CD3624C551D0515C4  # Matthew Heon <mheon@redhat.com>
  7CE1E6F8C90CB53E7E4D8F2D502E08DB0BBF8EEE  # Ashley Cui <acui@redhat.com>
  9E33DD8704CC03E2DEB84D9A1C1EDD7CC7C3A0DD  # Lokesh Mandvekar <lsm5@redhat.com>
)
sha256sums=('SKIP'
            'eeacf654707b9b8d6a6c08453b5625d9cf31010d666f82f4851aa34433b97700')

pkgver() {
  cd $pkgname
  git describe --tags | sed 's/^v//;s/-/+/g'
}

prepare() {
  # set default init_path to /usr/lib/podman/catatonit
  # https://bugs.archlinux.org/task/75493
  # https://github.com/containers/common/issues/1110
  patch -Np1 -d $pkgname -i ../$pkgname-4.6.0-defaultinitpath.patch
}

build() {
  # NOTE: the BUILDTAGS may change over time
  export BUILDTAGS='apparmor seccomp systemd'
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie"
  export GOPATH="${srcdir}"

  make -j1 EXTRA_LDFLAGS='-compressdwarf=false -linkmode=external' PREFIX=/usr -C $pkgbase
  make docker-docs -C $pkgbase
}

package_podman() {
  depends=(
    catatonit
    conmon
    containers-common
    crun
    gcc-libs
    glibc
    iptables
    device-mapper libdevmapper.so
    gpgme libgpgme.so
    libseccomp libseccomp.so
    slirp4netns
  )
  optdepends=(
    'apparmor: for AppArmor support'
    'btrfs-progs: support btrfs backend devices'
    'cni-plugins: for an alternative container-network-stack implementation'
    'fuse-overlayfs: for storage driver in rootless environment'
    'passt: for alternative rootless network support'
    'podman-compose: for docker-compose compatibility'
    'podman-docker: for Docker-compatible CLI'
  )

  make install install.completions DESTDIR="$pkgdir" PREFIX=/usr LIBEXECDIR=/usr/lib -C $pkgbase

  # Holo: remove podman-remote, it's quite big and we don't need it
  rm -f "$pkgdir/usr/bin/podman-remote"
  rm -f "$pkgdir/usr/share/bash-completion/completions/podman-remote"
  rm -f "$pkgdir/usr/share/fish/vendor_completions.d/podman-remote.fish"
  rm -f "$pkgdir/usr/share/man/man1/podman-remote.1"
  rm -f "$pkgdir/usr/share/zsh/site-functions/_podman-remote"
}

package_podman-docker() {
  pkgdesc='Emulate Docker CLI using podman'
  depends=(
    podman
    sh
  )
  conflicts=(docker)
  provides=(docker)

  make -j1 install.docker-full DESTDIR="$pkgdir" PREFIX=/usr -C $pkgbase
}
