% Úplná nehodnocená kontrola pro cvičení 2. Zdrojová data nemění.
fprintf('MATLAB: %s\nPracovní složka: %s\n', version, pwd);
assert(isfile('mereni_teploty.csv'), ...
    'Nahrajte mereni_teploty.csv a nastavte jeho složku jako Current Folder.');
data = readtable('mereni_teploty.csv');
assert(isequal(data.Properties.VariableNames, {'t', 'T'}), ...
    'Očekáváme hlavičku t,T.');
assert(height(data) == 241 && width(data) == 2, ...
    'Očekáváme 241 řádků a dva sloupce.');
assert(isnumeric(data.t) && isnumeric(data.T), 'Sloupce musí být číselné.');
assert(all(isfinite(data.t)) && all(isfinite(data.T)), ...
    'Data musí být konečná čísla.');
plot(data.t, data.T, '.-');
xlabel('t [s]'); ylabel('T [°C]'); grid on;
title('Kontrola prostředí — dodané měření teploty');
disp('OK: sloupce t,T; 241 řádků. Pokud vidíte graf, kontrola je dokončena.');
