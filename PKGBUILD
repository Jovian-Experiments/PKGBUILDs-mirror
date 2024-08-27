# Maintainer: Changwoo Min <changwoo@igalia.com>
# Maintainer: Tejun Heo <tj@kernel.org>
# Maintainer: Peter Jung ptr1337 <admin@ptr1337.dev>
# Maintainer: Piotr Górski <lucjan.lucjanov@gmail.com>

pkgname=scx-scheds
gitname=scx
pkgver=1.0.3.linux.neptune.68
pkgrel=7
pkgdesc="sched_ext schedulers"
arch=('x86_64')
url="https://gitlab.steamos.cloud/holo/scx/-/tree/v$pkgver"
license=('GPL-2.0-only')
depends=('libelf' 'zlib' 'jq')
makedepends=('git' 'openssh' 'python' 'meson' 'clang' 'llvm' 'llvm-libs' 'rust' 'cargo')
backup=('etc/default/scx' 'etc/systemd/journald@sched-ext.conf')
source=("git+ssh://git@gitlab.steamos.cloud/holo/scx.git#tag=v$pkgver")
sha256sums=('SKIP')
options=(!lto)
provides=("scx-scheds=$pkgver")
conflicts=(
  "scx-scheds-git"
)

_backports=(
)

_reverts=(
)

prepare() {
 export RUSTUP_TOOLCHAIN=stable
 cd $gitname

 local _c _l
  for _c in "${_backports[@]}"; do
    if [[ "${_c}" == *..* ]]; then _l='--reverse'; else _l='--max-count=1'; fi
    git log --oneline "${_l}" "${_c}"
    git cherry-pick --mainline 1 --no-commit "${_c}"
  done
  for _c in "${_reverts[@]}"; do
    if [[ "${_c}" == *..* ]]; then _l='--reverse'; else _l='--max-count=1'; fi
    git log --oneline "${_l}" "${_c}"
    git revert --mainline 1 --no-commit "${_c}"
  done

  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    [[ $src = *.patch ]] || continue
    echo "Applying patch $src..."
    patch -Np1 < "../$src"
  done
}

build() {
  cd $gitname
  arch-meson . build --buildtype release --auto-features auto
  meson compile -C build
}

package() {
  cd $gitname
  install -Dm644 "services/scx" "${pkgdir}/etc/default/scx"
  install -Dm644 "services/systemd/journald@sched-ext.conf" "${pkgdir}/etc/systemd/journald@sched-ext.conf"
  install -Dm644 "services/systemd/scx.service" "${pkgdir}/usr/lib/systemd/system/scx.service"
  install -Dm644 "libalpm/systemd/90-scx-scheds-upgrade.hook" "${pkgdir}/usr/share/libalpm/hooks/90-scx-scheds-upgrade.hook"
  install -Dm755 "libalpm/systemd/scx-systemd-restart" "${pkgdir}/usr/share/libalpm/scripts/scx-systemd-restart"
  install -Dm755 "build/scheds/rust/release/scx_lavd" "${pkgdir}/usr/bin/scx_lavd"
  install -Dm644 "LICENSE" "${pkgdir}/usr/share/licenses/$pkgname/LICENSE"
}
